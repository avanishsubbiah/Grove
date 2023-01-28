package io.grove

import io.micronaut.serde.annotation.Serdeable
import javax.validation.constraints.NotBlank

@Serdeable
data class UserUpdateCommand(
    val id: Long,
    @field: NotBlank val name: String
)
