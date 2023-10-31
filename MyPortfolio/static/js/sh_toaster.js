
const Toast = {
  success(message, Settings = []) {
    this._showToast(message, 'success', Settings);
  },
  danger(message, Settings = []) {
    this._showToast(message, 'danger', Settings);
  },
  warning(message, Settings = []) {
    this._showToast(message, 'warning', Settings);
  },
  info(message, Settings = []) {
    this._showToast(message, 'info', Settings);
  },

  _showToast(message, type, Settings){
    let duration = Settings.duration || 3000; // Default duration in milliseconds
    let showProgress = Settings.showProgress || false;
    let toastLocation = Settings.toastLocation || 'bottom'; // top / bottom

    const toastContainers = {
      top: document.getElementById('shToastContainerTop'),
      bottom: document.getElementById('shToastContainerBottom'),
    };

    const shToastContainer = toastContainers[toastLocation];
    const toast = document.createElement('div');
    toast.classList.add('sh-toast', type);
    toast.textContent = message;

    const progressBar = document.createElement('div');
    progressBar.classList.add('sh-progress-bar');

    if(showProgress) {
      toast.classList.add('with-sh-progress-bar');
      progressBar.style.width = '0';
      toast.appendChild(progressBar);
    }

    shToastContainer.appendChild(toast);
    // removing previous location and then set new one
    shToastContainer.classList.remove('top', 'bottom');
    shToastContainer.classList.add(toastLocation);

    const startTimestamp = Date.now();

    function updateProgressBar() {
      const elapsedTime = Date.now() - startTimestamp;
      const remainingTime = Math.max(0, duration - elapsedTime);
      const percentage = (remainingTime / duration) * 100;
      progressBar.style.width = `${percentage}%`;

      if (remainingTime > 0) {
        requestAnimationFrame(updateProgressBar);
      } else {
        shToastContainer.removeChild(toast);
      }
    }

    requestAnimationFrame(updateProgressBar);
  }


};




document.getElementById('MyForm').addEventListener('submit', function (e) {
  e.preventDefault();  // Prevent the default form submission

  // Get form data
  var formData = new FormData(this);

  // Send the data to the server using AJAX
  fetch('api/post/form', {
      method: 'POST',
      body: formData,
  })
  .then(response => response.json())
  .then(data => {
     
      if (data.success) {
        Toast.success('Form submitted successfully!',{
          showProgress: true,
        });
        
         
      } else {
        Toast.success('Form submission failed:',{
          showProgress: true,
        });
        
      }
  })
  .catch(error => {
      console.error('An error occurred:', error);
  });
});

