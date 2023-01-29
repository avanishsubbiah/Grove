<div class="home-page"> 
  <!-- justify-center content-center -->
  <!-- <img class="flex container justify-center content-center" src="/lifeCycle.png"> -->
  <br>
  <!-- <div id="conversationCard" class="mycards col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <br> -->
    <!-- <img src="/polaroid.png"> -->
    <p class="text-center font-serif text-medium text-xl" style="margin: 1.5rem"> Welcome to your Grove</p>
  <!-- </div> -->
  <br>
  <div id="conversationCard" class="col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <p class="text-center font-serif text-medium text-xl" style="margin: 1.5rem"> Talk to Ramune about his latest artwork!</p>
    <!-- <p> Talk to {friend} about {topic}!</p> -->
  </div>
  <br>
  <div id="treeCard" class="mycards col-md-12 card container shadow-xl sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <div style="margin: 1.5rem;">
      <span>
        <h4 class="text-left text-xl font-serif text-medium">Your Trees<span style="float:right">Statuses</span></h4>
      </span>
      <hr>
      {#each dispTrees() as tree}
      <div id="treeEntries" class="sm:rounded-lg sm:pt-3 sm:pb-3">
        <p> <a href="/tree?treeID={tree.treeID}">{tree.name}</a> <span style="float:right">{tree.status}</span></p>
        <hr>
      </div>
      {/each}
    </div>
  </div>
</div>

<script>
  let trees = [
    { treeID: 1, name: "Ramune", status: "Happy b/c sushi"},
    { treeID: 2, name: "Fanta", status: "Missing my GF hours"},
    { treeID: 3, name: "Rosé", status: "It's a wine kind of night" },
  ]

  function dispTrees() {
    return trees;
  }
</script>

<style lang="postcss">

</style>