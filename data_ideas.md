# Ideas for queries

## Friends

```
[api-url]/friends =>
{
    friends : [
        { id: "1", firstName: "foo", lastName: "bar"},
        { id: "2", firstName: "foo1", lastName: "bar"},
        { id: "3", firstName: "deez", lastName: "nutz"}
    ]
}

[api-url]/friends/lastName=bar =>
{
    friends : [
        { id: "1", firstName: "foo", lastName: "bar"},
        { id: "2", firstName: "foo1", lastName: "bar"}
    ]
}

[api-url]/friends/id=[friend_id] =>
{
    id: "1",
    firstName: "foo",
    lastName: "bar",
    status: "being cringe 😂", // Current status
    relationship: "" // Type of relationship
}   
```

### Trees

```
[api-url]/trees =>
{
    trees : [
        { id: "4", friendID: "1"},
        { id: "2", friendID: "2"},
        { id: "3", friendID: "3"}
    ]
}

[api-url]/trees/friend_ID=[friend_id] =>
{
    id: "4",
    friendID: "1",
    growthStage: 6
}

[api-url]/trees/id=[tree_id] =>
{
    id: "4",
    friendID: "1",
    growthStage: 6
}   
```

### Quests

```

[api-url]/quests/friend_ID=[friend_id] =>
{
    id: "4",
    friendID: "1",
    quests: [
        { dateTime: 13243545, content: "Take pic of reeeee", status: "Completed" },
        { dateTime: 13243546, content: "Watch Morbius", status: "Incomplete" },
        ...
    ]
}
```

### Notifications

```

[api-url]/noti =>
{
    notis: [
        { dateTime: 13435556, content: "Booped by Foo Bar", status: "active" },
        { dateTime: 13435557, content: "Growth with Foo Bar increased!", status: "active" },
        { dateTime: 13435558, content: "New quest with Deez Nutz!", status: "inactive" },
    ]
}
```
