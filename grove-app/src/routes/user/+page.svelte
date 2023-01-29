<script>
    import {onMount} from 'svelte';
    import {authenticated} from '../../stores/auth';
    let message = ''
    onMount(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/user', {
                headers: {'Content-Type': 'application/json'},
                credentials: 'include',
            });
            const content = await response.json();
            message = `Hi ${content.name}`;
            authenticated.set(true);
        } catch (e) {
            message = 'You are not logged in';
            authenticated.set(false);
        }
    });

    import {goto} from "$app/navigation";
    let username = '', password = ''
    const submit = async () => {
        await fetch('http://localhost:8000/api/token', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            credentials: 'include',
            body: JSON.stringify({
                username,
                password
            })
        });
        await console.log(response.json());
    }
</script>

<form on:submit|preventDefault={submit}>
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <input bind:value={username} type="username" class="form-control" placeholder="username" required>

    <input bind:value={password} type="password" class="form-control" placeholder="Password" required>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
</form>

{message}