<div class="home-page"> 
  <!-- justify-center content-center -->
  <br>
  <div id="conversationCard" class="mycards col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <p style="margin: 1.5rem"> Talk to FRIEND about TOPIC!</p>
    <!-- <p> Talk to {friend} about {topic}!</p> -->
  </div>
  <br>
  <div id="treeCard" class="mycards col-md-12 card container shadow-xl sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <div style="margin: 1.5rem;">
      <span>
        <h4 class="text-left text-xl text-serif text-medium">Your Trees<span style="float:right">Statuses</span></h4>
      </span>
      <hr>
      {#each dispTrees() as tree}
      <div id="treeEntries" class="sm:rounded-lg sm:pt-3 sm:pb-3">
        <p> {tree.name} <span style="float:right">{tree.status}</span></p>
        <hr>
      </div>
      {/each}
    </div>
  </div>
</div>

<script>
  let trees = [
    { name: "Ramune", status: "Happy b/c sushi"},
    { name: "Fanta", status: "Missing my GF hours"},
    { name: "Rosé", status: "It's a wine kind of night" },
  ]

  function dispTrees() {
    return trees;
  }
</script>

<style lang="postcss">

</style>