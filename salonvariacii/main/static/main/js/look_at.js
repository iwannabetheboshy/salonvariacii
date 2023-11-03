$(document).ready(function() {
    const player = document.getElementByClassName('.like_btn');

    player.addEventListener('ready', () => {
        LottieInteractivity.create({
            player: player.getLottie(),
            mode:"cursor",
            actions: [
                {
                    type: "click",
                    forceFlag: false
                }
            ]
        });
    });

    $('.like_btn').on("click", function(){
        $('.like').toggle();
    });

})