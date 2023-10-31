const player = document.getElementById('like');

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