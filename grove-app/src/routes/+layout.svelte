<script>
	import '../app.scss';
</script>

<nav class="navbar navbar-expand-sm navbar-toggleable-sm border-bottom box-shadow container">
  <a href="/noti" class="col-md-3 text-left"><img class="text-3xl max-h-7 max-w-xs flex" src="/bell.png" alt="Notifs"/></a>
  <a href="/" class="col-md-6 text-center text-3xl font-serif font-medium">Grove</a>  
  <a href="/wishlist?treeID=1" class="col-md-3 text-right">Wishlist</a>
  <a href="/user" class="col-md-3">User</a>
</nav>

<slot></slot>
<style lang="postcss">
  .mycards {
		margin: 1.5rem;
  }
</style>