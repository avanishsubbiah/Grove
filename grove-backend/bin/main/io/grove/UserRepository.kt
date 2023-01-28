package io.grove

import io.grove.domain.User
import io.micronaut.data.annotation.Id
import io.micronaut.data.exceptions.DataAccessException
import io.micronaut.data.model.query.builder.sql.Dialect
import io.micronaut.data.r2dbc.annotation.R2dbcRepository
import io.micronaut.data.repository.reactive.ReactorPageableRepository
import reactor.core.publisher.Mono
import javax.transaction.Transactional
import javax.validation.constraints.NotBlank

@R2dbcRepository(dialect = Dialect.MYSQL)
abstract class UserRepository : ReactorPageableRepository<User, Long> {
    abstract fun save(@NotBlank name: String) Mono<User>

    @Transactional
    open fun saveWithException(@NotBlank name: String): Mono<User> {
        return save(name).then(Mono.error(DataAccessException("test exception")))
    }

    abstract fun update(@Id id: Long, @NotBlank name: String): Mono<Long>
}
