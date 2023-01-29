<div class="container col-lg-12">
    <br>
    <span>
        <h1 class="flex justify-center text-2xl font-light font-serif">
            {treeNameFromID(treeID)}'s Wishlist
        </h1>
    </span>
    <span class="container"> 
        <img style="max-width: 25rem" class="container-fluid" src="/stage0.png" alt="Tree">
    </span>
    <div class="card container sm:max-w-lg sm:rounded-lg">
        <div class="mycards container-content sm:mx-auto  sm:px-10"> 
            <h1 class="flex justify-center text-3xl font-light font-serif">Quests</h1>
        </div>
    </div>
    <br>
    <div id="treeSettingsCard" class="card container sm:max-w-lg sm:rounded-lg">
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
        { item: "Ceramic Mug", url: "", status: "active" },
        { item: "Hydroflask", url: "", status: "active" },
        { item: "Nail Polish", url: "", status: "active" },
        { item: "Ice Cream", url: "", status: "active" },
    ]

    function dispWishlist() {
        return wishlist
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
    .checkbox {
    --background: #fff;
    --border: #D1D6EE;
    --border-hover: #BBC1E1;
    --border-active: #1E2235;
    --tick: #fff;
    position: relative;
    input,
    svg {
        width: 21px;
        height: 21px;
        display: flex;
    }
    input {
        -webkit-appearance: none;
        -moz-appearance: none;
        position: relative;
        outline: none;
        background: var(--background);
        border: none;
        margin: 0;
        padding: 0;
        cursor: pointer;
        border-radius: 4px;
        transition: box-shadow .3s;
        box-shadow: inset 0 0 0 var(--s, 1px) var(--b, var(--border));
        &:hover {
            --s: 2px;
            --b: var(--border-hover);
        }
        &:checked {
            --b: var(--border-active);
        }
    }
    svg {
        pointer-events: none;
        fill: none;
        stroke-width: 2px;
        stroke-linecap: round;
        stroke-linejoin: round;
        stroke: var(--stroke, var(--border-active));
        position: absolute;
        top: 0;
        left: 0;
        width: 21px;
        height: 21px;
        transform: scale(var(--scale, 1)) translateZ(0);
    }
    &.path {
        input {
            &:checked {
                --s: 2px;
                transition-delay: .4s;
                & + svg {
                    --a: 16.1 86.12;
                    --o: 102.22;
                }
            }
        }
        svg {
            stroke-dasharray: var(--a, 86.12);
            stroke-dashoffset: var(--o, 86.12);
            transition: stroke-dasharray .6s, stroke-dashoffset .6s;
        }
    }
    &.bounce {
        --stroke: var(--tick);
        input {
            &:checked {
                --s: 11px;
                & + svg {
                    animation: bounce .4s linear forwards .2s;
                }
            }
        }
        svg {
            --scale: 0;
        }
    }
}
</style>