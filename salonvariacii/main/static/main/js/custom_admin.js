document.addEventListener('DOMContentLoaded', function () {
  const styleSelect = document.getElementById('id_style');
  const materialSelect = document.getElementById('id_material');
  const openingMethodSelect = document.getElementById('id_openingMethod');

  styleSelect.addEventListener('change', function () {
    const styleId = styleSelect.value;

    fetch('/get-related-items-for-admin/?styles=' + styleId)
      .then(response => response.json())
      .then(data => {

        materialSelect.innerHTML = '<option value="" selected>---------</option>';
        data.materials.forEach(material => {
          const option = document.createElement('option');
          option.value = material.id;
          option.textContent = material.name;
          materialSelect.appendChild(option);
        });

        openingMethodSelect.innerHTML = '<option value="" selected>---------</option>';
        data.opening_methods.forEach(openingMethod => {
          const option = document.createElement('option');
          option.value = openingMethod.id;
          option.textContent = openingMethod.name;
          openingMethodSelect.appendChild(option);
        });
      });
  });
});
