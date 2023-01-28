package io.grove.domain

import io.micronaut.serde.annotation.Serdeable
import io.micronaut.data.annotation.GeneratedValue
import io.micronaut.data.annotation.Id
import io.micronaut.data.annotation.MappedEntity


@Serdeable
@MappedEntity
data class User(
    @field: Id
    @field: GeneratedValue(GeneratedValue.Type.AUTO)
    var id: Long? = null,
    var name: String
)
