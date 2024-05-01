    document.addEventListener('DOMContentLoaded', function() {
      const languageSelect = document.getElementById('language');
      const modelSelect = document.getElementById('model');
      const inputText = document.getElementById('inputText');
      const generateSummaryButton = document.getElementById('generateSummary');
      const summaryDiv = document.getElementById('summary');

      // Populate model options based on selected language
      function populateModels(language) {
        const models = {
          en: ['T5', 'BART'],
          uk: ['mT5']
        };

        // Clear existing options
        modelSelect.innerHTML = '';

        // Populate model selection with appropriate options
        models[language].forEach(function(model) {
          const option = document.createElement('option');
          option.value = model;
          option.textContent = model;
          modelSelect.appendChild(option);
        });
      }

      // Event listener for language selection change
      languageSelect.addEventListener('change', function() {
        populateModels(languageSelect.value);
      });

      // Initial population of models
      populateModels(languageSelect.value);

      // Send data to the backend and display summary
        function generateSummary() {
          const data = {
            language: languageSelect.value,
            model: modelSelect.value,
            text: inputText.value
          };

          // Send data to your Django backend
          fetch('/generate_summary/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
          })
          .then(response => response.json())
          .then(data => {
            const summaryText = data.summary;
            summaryDiv.textContent = "";
            let index = 0;
            const interval = setInterval(function() {
              summaryDiv.textContent += summaryText[index];
              index++;
              if (index >= summaryText.length) {
                clearInterval(interval);
              }
            }, 50); // Interval to control the speed of typing effect
            summaryDiv.style.display = 'block';
          })
          .catch((error) => {
            console.error('Error:', error);
          });
        }

      // Event listener for button click
      generateSummaryButton.addEventListener('click', generateSummary);
    });