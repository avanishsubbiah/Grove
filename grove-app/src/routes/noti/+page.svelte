<div class="noti">
  <div class="header">
  </div>
  <div class="noti-list">
    {#each dispNotis() as noti}
      <div id="noti-card" class="col-md-12 container shadow-xl our-bg p-auto rounded sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10 sm:pt-5 sm:pb-5">
        <!-- {#if noti.type == doQuest}
          <p> {noti.content} 
            <span style="float:right">
              {formatTime(noti.dateTime)} {formatDate(noti.dateTime)}
            </span>
          </p>
        {:else if noti.type == viewQuest}
          <p> {noti.content} 
            <span style="float:right">
              {formatTime(noti.dateTime)} {formatDate(noti.dateTime)}
            </span>
          </p>
        {:else} -->
        <p style="margin: .5rem"> {noti.content} 
          <span style="float:right">
            {formatTime(noti.dateTime)} {formatDate(noti.dateTime)}
          </span>
        </p>
        <!-- {/if} -->
      </div>
    {/each}
  </div>
</div>

<script>
  let notis = [
    { dateTime: 1674939694, content: "Shaken by Foo Bar", status: "active" , type:"shake"},
    { dateTime: 1674939695, content: "Growth with Foo Bar increased!", status: "active", type:"milestone" },
    { dateTime: 1674939696, content: "You Recieved a Quest from Ramune! Take a funny picture", status: "active", type:"doQuest" },
    { dateTime: 1674939696, content: "Ramune sent you their Quest! Here's what they ate for dinner", status: "active", type:"viewQuest"},
  ]

  function dispNotis() {
    return notis.filter(function (el)
      {
        return el.status === "active";
      }
    );
  }

  function formatTime(unixTimestamp) {
    // Create a new JavaScript Date object based on the timestamp
    // multiplied by 1000 so that the argument is in milliseconds, not seconds.
    var date = new Date(unixTimestamp * 1000);
    // Hours part from the timestamp
    var hours = date.getHours();
    // Minutes part from the timestamp
    var minutes = "0" + date.getMinutes();
    // Seconds part from the timestamp
    var seconds = "0" + date.getSeconds();
    

    // Will display time in 10:30:23 format
    // var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
    
    var formattedTime = hours + ':' + minutes.substr(-2);
    return formattedTime;
  }

  function formatDate(unixTimestamp) {
    var date = new Date(unixTimestamp * 1000);
    var day = date.getDate()
    var month = date.getMonth() + 1;
    var year = date.getFullYear();
    var formattedDate = day + "/" + month + "/" + year;
    return formattedDate;
  }

  console.log(dispNotis());
</script>

<style lang="postcss">
</style>