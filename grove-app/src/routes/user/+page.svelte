<script>
    import {onMount} from 'svelte';
    import {accessTok, refreshTok} from '../../stores/auth';
    let message = ''
    // onMount(async () => {
    //     try {
    //         const response = await fetch('http://localhost:8000/api/user', {
    //             headers: {'Content-Type': 'application/json'},
    //             credentials: 'include',
    //         });
    //         const content = await response.json();
    //         message = `Hi ${content.name}`;
    //         authenticated.set(true);
    //     } catch (e) {
    //         message = 'You are not logged in';
    //         authenticated.set(false);
    //     }
    // });

    import {goto} from "$app/navigation";
    let username = '', password = ''
    async function submit() {
        try {
            const response = await fetch('http://localhost:8000/api/token/', {
                method: 'POST',
                headers: {'Content-type': 'application/json'},
                body: JSON.stringify({"username": username, "password": password})
            });
            const content = await response.json();
            $accessTok = content.access;
            $refreshTok = content.refresh;
            message = `Hi ${JSON.stringify(content)}`;
        } catch (e) {
            message = 'You are not logged in';
        }
    }
    
    let num_tries = 0;

    async function dispFren() {
        try {
            const response = await fetch('http://localhost:8000/users/friends/', {
                method: 'GET',
                headers: {'Content-type': 'application/json', 'Authorization': `Bearer ${$accessTok}`},
            });
            const content = await response.json();
            if (content.code === "token_not_valid") {
                try {
                    const response = await fetch('http://localhost:8000/api/token/refresh/', {
                        method: 'POST',
                        headers: {'Content-type': 'application/json'},
                        body: JSON.stringify({"refresh": $refreshTok})
                    });
                    const content = await response.json();
                    if (content.hasOwnProperty('access')) {
                        $accessTok = content.access;
                        if (num_tries < 5) {
                            num_tries += 1;
                            dispFren();
                        } else {
                            console.log("Try Logging in Again");
                            num_tries = 0;
                            return;
                        }
                    } else {
                        console.log("Cope and mald");
                    }
                    message = `Hi ${JSON.stringify(content)}`;
                } catch (e) {
                    goto('/user');
                }
            } else {
                message = `Your Frens: ${JSON.stringify(content)}`;
            }
        } catch (e) {
            message = 'You are not logged in';
        }
    }

    function logout() {
        $accessTok = null;
        $refreshTok = null;
    }
    
</script>

<form on:submit|preventDefault={submit}>
    <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

    <input bind:value={username} type="username" class="form-control" placeholder="username" required>

    <input bind:value={password} type="password" class="form-control" placeholder="Password" required>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
</form>

<button class="w-100 btn btn-lg btn-primary" on:click={logout}>Sign out</button>

<button class="w-100 btn btn-lg btn-primary" on:click={dispFren}>No frens?</button>

{message}