<script>
    let videoSource = null;
    let loading = false;
    let stream;
    const obtenerVideoCamara = async () => {
      try {
        loading = true;
        stream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        videoSource.srcObject = stream;
        videoSource.play();
        loading = false;
      } catch (error) {
        console.log(error);
      }
    };

    function getImage() {
        canvas.getContext('2d').drawImage(videoSource, 0, 0, canvas.width, canvas.height);
        let image_data_url = canvas.toDataURL('image/jpeg');

        // data url of the image
        console.log(image_data_url);
    }

    function stopBothVideoAndAudio() {
        stream.getTracks().forEach(function(track) {
            if (track.readyState == 'live') {
                track.stop();
            }
        });
    }
  </script>
  
  <div>
    {#if loading}
      <h1>LOADING</h1>
    {/if}
    <!-- svelte-ignore a11y-media-has-caption -->
    <video bind:this={videoSource} width="320" height="240" />
    <canvas id="canvas" width="320" height="240"></canvas>
    <button on:click={obtenerVideoCamara} class="btn btn-lg btn-success active">Start Camera</button>
    <button on:click={getImage} class="btn btn-lg btn-success active">Take Photo</button>
    <button on:click={stopBothVideoAndAudio} class="btn btn-lg btn-success active">Stop Camera</button>
  </div>