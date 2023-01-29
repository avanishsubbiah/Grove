<div class="container col-lg-12">
    <br>
    <span>
        <h1 class="flex justify-center text-2xl font-light font-serif">
            {treeNameFromID(treeID)}'s Wishlist
        </h1>
    </span>
    <div class="our-bg p-1 rounded shadow-xl container sm:max-w-lg sm:rounded-lg">
        <div class="mycards container-content sm:mx-auto"> 
            <div class="grid grid-cols-3">
                <div>
                    <h4 class="">Purchased?</h4>
                    <hr>
                    {#each dispWishlist() as entry}
                        <p> {entry.status}</p>
                    {/each}
                </div>
                <div>
                    <h4 class="">Item</h4>
                    <hr>
                    {#each dispWishlist() as entry}
                        <p> {entry.item}</p>
                    {/each}
                </div>
                <div>
                    <h4 class="">URL</h4>
                    <hr>
                    {#each dispWishlist() as entry}
                        <a href={entry.url}> Link</a><br>
                    {/each}
                </div>
            </div>
        </div>
    </div>
    <br>
    <div id="treeSettingsCard" class="our-bg p-1 rounded container shadow-xl sm:max-w-lg sm:rounded-lg">
        <div class="mycards container-content sm:mx-auto sm:px-10"> 
            <h1 class="flex justify-center text-3xl font-light font-serif">Settings</h1>
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchRomantic" checked>
                <label class="form-check-label" for="flexSwitchRomantic">Visible</label>
            </div>
        </div>
    </div>
    <br>
</div>

<script>
    import { page } from '$app/stores';
    const treeID = parseInt($page.url.searchParams.get('treeID'), 10);

    let trees = [
        { treeID: 1, name: "Ramune", status: "Happy b/c sushi"},
        { treeID: 2, name: "Fanta", status: "Missing my GF hours"},
        { treeID: 3, name: "Rosé", status: "It's a wine kind of night" },
    ]

    let wishlist = [
        { item: "Ceramic Mug", url: "https://www.swellceramics.com/", status: "true" },
        { item: "Hydroflask", url: "https://www.hydroflask.com/?msclkid=be468092a1b113752856e3474c8cb7e9", status: "true" },
        { item: "Nail Polish", url: "https://www.cirquecolors.com/", status: "false" },
        { item: "Ice Cream", url: "https://milkbarstore.com/collections/the-ice-cream-shop", status: "true" },
    ]

    function dispWishlist() {
        return wishlist;
        // .filter(function (el)
        // {
        //     return el.status === "active";
        // }
        // );
    }

    function treeNameFromID(id) {
        return trees.filter(obj => {
            return obj.treeID === id
        })[0].name
    }
</script>

<style lang="postcss">
    .mycards {
		margin: 1.5rem;
    }
</style>