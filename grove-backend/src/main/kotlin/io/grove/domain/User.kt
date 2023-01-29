package io.grove.domain

import io.micronaut.serde.annotation.Serdeable
import io.micronaut.data.annotation.GeneratedValue
import io.micronaut.data.annotation.Id
import io.micronaut.data.annotation.MappedEntity
import javax.validation.constraints.NotBlank

@MappedEntity
class Users(var name: @NotBlank String?, var username: @NotBlank String?) {
    
}