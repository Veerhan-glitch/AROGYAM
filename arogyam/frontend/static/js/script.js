const apiUrl = 'http://127.0.0.1:8000/api';
const output = document.getElementById('output');

function show(data) {
  output.innerText = JSON.stringify(data, null, 2);
}

function getUserOrders() {
  const userId = document.getElementById('user_id').value;
  if (!userId) {
    alert('Please enter a user id');
    return;
  }
  axios.get(`${apiUrl}/orders/?userid=${userId}`)
    .then(response => show(response.data))
    .catch(error => console.error(error));
}

function getUserAppointments() {
  const userId = document.getElementById('user_id').value;
  if (!userId) {
    alert('Please enter a user id');
    return;
  }
  axios.get(`${apiUrl}/appointments/?userid=${userId}`)
    .then(response => show(response.data))
    .catch(error => console.error(error));
}

function getUserPrescriptions() {
  const userId = document.getElementById('user_id').value;
  if (!userId) {
    alert('Please enter a user id');
    return;
  }
  axios.get(`${apiUrl}/prescriptions/?userid=${userId}`)
    .then(response => show(response.data))
    .catch(error => console.error(error));
}

// New function to get feedback based on order id
function getFeedback() {
  const orderId = document.getElementById('order_id').value;
  if (!orderId) {
    alert('Please enter an order id');
    return;
  }
  axios.get(`${apiUrl}/feedback/?orderid=${orderId}`)
    .then(response => show(response.data))
    .catch(error => console.error(error));
}

// Existing functions remain unchanged
function getAllDoctors() {
  axios.get(`${apiUrl}/doctors/`)
    .then(response => show(response.data))
    .catch(error => console.error(error));
}

function uploadPrescription() {
  axios.post(`${apiUrl}/prescriptions/`, {
      userid: 1,
      details: "Test Prescription"
  })
  .then(response => show(response.data))
  .catch(error => console.error(error));
}

function bookAppointment() {
  axios.post(`${apiUrl}/appointments/`, {
      userid: 1,
      doctorid: 2,
      date: "2025-04-10"
  })
  .then(response => show(response.data))
  .catch(error => console.error(error));
}

function giveFeedback() {
  axios.post(`${apiUrl}/feedback/`, {
      userid: 1,
      message: "Great Service!"
  })
  .then(response => show(response.data))
  .catch(error => console.error(error));
}

function orderProducts() {
  axios.post(`${apiUrl}/orders/`, {
      userid: 1,
      date: "2025-04-10",
      status: "Pending"
  })
  .then(response => show(response.data))
  .catch(error => console.error(error));
}
