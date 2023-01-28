<div class="home-page"> 
  <!-- justify-center content-center -->
  <br>
  <div id="conversationCard" class="homecard col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <p style="margin: 1.5rem"> Talk to FRIEND about TOPIC!</p>
    <!-- <p> Talk to {friend} about {topic}!</p> -->
  </div>
  <br>
  <div id="treeCard" class="homecard col-md-12 card container shadow-xl sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
    <div style="margin: 1.5rem;">
      <h4>Your Trees</h4>
      <hr>
      <!-- Trees as blocks -->
      <!-- {#each trees as tree (tree.id)}
        <Tree current={tree.color}/>
      {/each} -->
    </div>
  </div>
</div>
<style lang="postcss">
  .homecard {
		margin: 5 rem;
  }
</style>