document.addEventListener('DOMContentLoaded', function () {
    const kitchenCardVideo = document.getElementsByClassName('field-kitchenCardVideo')[0];
    const kitchenCardPhoto = document.getElementsByClassName('field-kitchenCardPhoto')[0];
    
    kitchenCardVideo.style.display = "none";
    kitchenCardPhoto.style.display = "none";

    const select = document.getElementById('id_kitchenCardVideoPhotoChoices');
    if(select.value == 'photo'){
        kitchenCardPhoto.style.display = "block";
        kitchenCardVideo.style.display = "none";
    }else if(select.value == 'video'){
        kitchenCardVideo.style.display = "block";
        kitchenCardPhoto.style.display = "none";
    }

    select.addEventListener('change', function () {
        if(select.value == 'photo'){
            kitchenCardPhoto.style.display = "block";
            kitchenCardVideo.style.display = "none";
        }else if(select.value == 'video'){
            kitchenCardVideo.style.display = "block";
            kitchenCardPhoto.style.display = "none";
        }
    });
    
  });