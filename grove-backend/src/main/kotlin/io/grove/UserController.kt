package io.grove

import io.grove.domain.User
import io.micronaut.data.model.Pageable
import io.micronaut.http.HttpHeaders
import io.micronaut.http.HttpResponse
import io.micronaut.http.HttpStatus
import io.micronaut.http.MutableHttpHeaders
import io.micronaut.http.MutableHttpResponse
import io.micronaut.http.annotation.Body
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Delete
import io.micronaut.http.annotation.Get
import io.micronaut.http.annotation.Post
import io.micronaut.http.annotation.Put
import io.micronaut.http.annotation.Status
import java.net.URI
import javax.validation.Valid
import javax.validation.constraints.NotBlank
import reactor.core.publisher.Mono

@Controller("/users")
open class UserController(private val userRepository: UserRepository) {
    @Get("/{id}")
    fun show(id: Long): Mono<User> {
        return userRepository.findById(id)
    }

    @Put
    open fun update(@Body @Valid command: UserUpdateCommand): Mono<HttpResponse<*>> {
        return userRepository
                .update(command.id, command.name)
                .thenReturn(
                        HttpResponse.noContent<Any>()
                                .header(HttpHeaders.LOCATION, location(command.id).path)
                )
    }

    @Get("/list")
    open fun list(@Valid pageable: Pageable): Mono<List<User>> {
        return userRepository.findAll(pageable).map { it.content }
    }

    @Post
    open fun save(@NotBlank @Body("name") name: String): Mono<HttpResponse<User>> {
        return userRepository.save(name).map(this::createUser)
    }

    @Post("/ex")
    open fun saveExceptions(@NotBlank @Body name: String): Mono<MutableHttpResponse<User>> {
        return userRepository
                .saveWithException(name)
                .map(this::createUser)
                .onErrorReturn(HttpResponse.noContent())
    }

    @Delete("/{id}")
    @Status(HttpStatus.NO_CONTENT)
    fun delete(id: Long): Mono<Void> {
        return userRepository.deleteById(id).then()
    }

    private fun createUser(user: User): MutableHttpResponse<User> {
        return HttpResponse.created(user).headers { headers: MutableHttpHeaders ->
            headers.location(location(user))
        }
    }

    private fun location(id: Long?): URI {
        return URI.create("/users/$id")
    }

    private fun location(user: User): URI {
        return location(user.id)
    }
}
