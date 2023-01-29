<div class="home-page"> 
  <!-- justify-center content-center -->
  <!-- <img class="flex container justify-center content-center" src="/lifeCycle.png"> -->
  <br>
  <div id="conversationCard" class="mycards col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <br>
    <img src="/polaroid.png">
    <p class="text-center font-serif text-medium text-xl" style="margin: 1.5rem"> Welcome to your Grove</p>
    <!-- <p> Talk to {friend} about {topic}!</p> -->
  </div>
  <br>
  <div id="conversationCard" class="mycards col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <p class="text-center font-serif text-medium text-xl" style="margin: 1.5rem"> Talk to FRIEND about TOPIC!</p>
    <!-- <p> Talk to {friend} about {topic}!</p> -->
  </div>
  <br>
  <div id="treeCard" class="mycards col-md-12 card container shadow-xl sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <div style="margin: 1.5rem;">
      <span>
        <h4 class="text-left text-xl font-serif text-medium">Your Trees<span style="float:right">Statuses</span></h4>
      </span>
      <hr>
      {#each friends as friend}
      <div id="treeEntries" class="sm:rounded-lg sm:pt-3 sm:pb-3">
        <p> <a href="/tree?treeID={0}">{friend.first_name}</a> <span style="float:right">{friend.status}</span></p>
        <hr>
      </div>
      {/each}
    </div>
  </div>
</div>

<script>
  import {onMount} from 'svelte';
  import {accessTok, refreshTok} from '../stores/auth';
  let friends = [];

  let trees = [
    { treeID: 1, name: "Ramune", status: "Happy b/c sushi"},
    { treeID: 2, name: "Fanta", status: "Missing my GF hours"},
    { treeID: 3, name: "Rosé", status: "It's a wine kind of night" },
  ]

  function dispTrees() {
    return trees;
  }

  onMount(async () => {
        try {
            dispFren();
        } catch (e) {
            console.log('You are not logged in');
        }
  });
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
              friends = content;
          }
      } catch (e) {
          message = 'You are not logged in';
      }
  }
</script>

<style lang="postcss">

</style>