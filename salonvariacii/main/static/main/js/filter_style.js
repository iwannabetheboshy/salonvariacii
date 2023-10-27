document.addEventListener('DOMContentLoaded', function () {
  const materialSelect = document.getElementById('id_material');
  const openingMethodSelect = document.getElementById('id_openingMethod');
  const styleCheckboxes = document.querySelectorAll('input[name="style"]');

  styleCheckboxes.forEach(styleCheckbox => {
    styleCheckbox.addEventListener('change', function () {
        let selectedStyles = Array.from(styleCheckboxes)
            .filter(checkbox => checkbox.checked)
            .map(checkbox => checkbox.value);

        if (selectedStyles.length == 0){
            selectedStyles = [1, 2];
        }
        materialSelect.innerHTML = '';
        openingMethodSelect.innerHTML = '';

        const stylesQueryParam = selectedStyles.join(',');

        fetch(`/get-related-items-for-admin/?styles=${stylesQueryParam}`)
            .then(response => response.json())
            .then(data => {

            let uniqueNames = {};
            data.materials.forEach(material => {
                if (!uniqueNames[material.name]) {
                    uniqueNames[material.name] = true;

                    const matDiv = document.createElement('div');
                  matDiv.innerHTML = `
                    <label for="id_material_${material.id}"><input type="checkbox" name="material" value="${material.name}" id="id_material_${material.id}">
                    ${material.name}</label>
                  `;
                  materialSelect.appendChild(matDiv);
                }
            });

            uniqueNames = {};
            data.opening_methods.forEach(openingMethod => {
                if (!uniqueNames[openingMethod.name]) {
                    uniqueNames[openingMethod.name] = true;
                    const opDiv = document.createElement('div');
                  opDiv.innerHTML = `
                <label for="id_openingMethod_${openingMethod.id}"><input type="checkbox" name="openingMethod" value="${openingMethod.name}" id="id_openingMethod_${openingMethod.id}">
                ${openingMethod.name}</label>
                  `;
                    openingMethodSelect.appendChild(opDiv);
                }
            });
        });
    });
  });
});
