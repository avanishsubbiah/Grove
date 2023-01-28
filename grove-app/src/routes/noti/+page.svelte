<div class="noti">
  <div class="header">
  </div>
  <div class="noti-list">
    {#each dispNotis() as noti}
      <div id="noti-card" class="homecard col-md-12 container shadow-xl card sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10 sm:pt-5 sm:pb-5">
        <p style="margin: 1.5rem"> {noti.content} <span style="float:right">{formatTime(noti.dateTime)} {formatDate(noti.dateTime)}</span></p>
        <!-- <p> Talk to {friend} about {topic}!</p> -->
      </div>
    {/each}
  </div>
</div>

<script>
  let notis = [
    { dateTime: 1674939694, content: "Booped by Foo Bar", status: "active" },
    { dateTime: 1674939695, content: "Growth with Foo Bar increased!", status: "active" },
    { dateTime: 1674939696, content: "New quest with Deez Nutz!", status: "inactive" },
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
    var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
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
  .homecard {
		margin: 5 rem;
  }
</style>