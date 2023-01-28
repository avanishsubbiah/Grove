<div class="container col-lg-12">
    <br>
    <span>
        <h1 class="flex justify-center text-2xl font-light font-serif">
            Ramune's Tree
        </h1>
        <p class="flex justify-center">Planted: DATE</p>
    </span>
    <span class="container"> 
        <img style="max-width: 25rem" class="container-fluid" src="/stage0.png" alt="Tree">
    </span>
    <div class="flex justify-center">
        <button type="submit" aria-disabled="false" class="btn btn-lg btn-success active">Shake</button>
    </div>
    <br>
    <p class="flex justify-center" style="display:none">You may shake again at TIME </p>
    
    <div class="card container sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
        <div class="mycards container-content"> 
            <h1 class="flex justify-center text-2xl font-light font-serif">Quests</h1>
            {#each dispQuests() as quest}
                <div id="questEntry" class="relative align-middle content-center">
                    <ul class=""> 
                        <label class="checkbox path">
                            <input type="checkbox">
                            <svg viewBox="0 0 21 21">
                                <path d="M5,10.75 L8.5,14.25 L19.4,2.3 C18.8333333,1.43333333 18.0333333,1 17,1 L4,1 C2.35,1 1,2.35 1,4 L1,17 C1,18.65 2.35,20 4,20 L17,20 C18.65,20 20,18.65 20,17 L20,7.99769186"></path>
                            </svg>
                        </label>
                        <span class="pb-3"> &nbsp;{quest.content}</span> 
                        <!-- I GIVE UP -->
                    </ul>
                </div>
            {/each}
        </div>
    </div>
    <br>
</div>

<script>
    let quests = [
        { dateTime: 1674939694, content: "Take a pic of your pet", status: "active" },
        { dateTime: 1674939695, content: "Whatcha Eating?", status: "active" },
        { dateTime: 1674939696, content: "Something Funny", status: "active" },
        { dateTime: 1674939696, content: "Whatcha Doing?", status: "inactive" },
    ]

    function dispQuests() {
        return quests.filter(function (el)
        {
            return el.status === "active";
        }
        );
    }
    // console.log(dispNotis());
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