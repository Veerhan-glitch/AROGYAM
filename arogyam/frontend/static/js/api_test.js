const API = '/api/';
    function showOutput(data) {
      document.getElementById('output').textContent = JSON.stringify(data, null, 2);
    }
    function callAPI(endpoint, method="POST", payload={}) {
      fetch(API + endpoint, {
          method,
          headers: { "Content-Type": "application/json" },
          body: method === "GET" ? null : JSON.stringify(payload)
      })
      .then(response => response.json())
      .then(data => showOutput(data))
      .catch(err => showOutput({ error: err.toString() }));
    }
    // ---------- CUSTOMER FUNCTIONS ----------
    function getPastOrders() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("orders/", "POST", { userid });
    }
    function getFeedbackByUser() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("feedback-by-user/", "POST", { userid });
    }
    function getFeedbackByProduct() {
      const productid = document.getElementById('prod_id').value;
      if (!productid) { alert("Enter Product ID!"); return; }
      callAPI("feedback-by-product/", "POST", { productid });
    }
    function getUserAppointments() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("user_appointments/", "POST", { userid });
    }
    function getUserPrescriptions() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("prescriptions/", "POST", { userid });
    }
    function bookAppointment() {
      const userid = document.getElementById('appt_userid').value;
      const doctorid = document.getElementById('appt_docid').value;
      const date = document.getElementById('appt_date').value;
      const type = document.getElementById('appt_type').value;
      if (!userid || !doctorid || !date || !type) {
        alert("Fill all fields for appointment booking.");
        return;
      }
      callAPI("book-appointment/", "POST", { userid, doctorid, date, type });
    }
    function getPaymentHistory() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("payment-history/", "POST", { userid });
    }
    function browseLabTests() {
      const name = document.getElementById('labtest_query').value;
      callAPI("labtests/", "POST", { name });
    }
    function viewReports() {
      const testid = document.getElementById('report_testid').value;
      if (!testid) { alert("Enter Test ID!"); return; }
      callAPI("reports/", "POST", { testid });
    }
    function submitSupportTicket() {
      const userid = document.getElementById('cust_userid').value;
      const issuetype = document.getElementById('ticket_type').value;
      const description = document.getElementById('ticket_desc').value;
      if (!userid || !issuetype || !description) {
        alert("Fill all support ticket fields.");
        return;
      }
      callAPI("submit-ticket/", "POST", { userid, issuetype, description });
    }
    function viewSupportTickets() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("support-tickets/", "POST", { userid });
    }
    function getUserNotifications() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("notifications/", "POST", { userid });
    }
    function getUserOffers() {
      const userid = document.getElementById('cust_userid').value;
      if (!userid) { alert("Enter your User ID!"); return; }
      callAPI("user-offers/", "POST", { userid });
    }
    function searchProducts() {
      const query = document.getElementById('prod_query').value;
      callAPI("search-products/", "POST", { query });
    }
    function viewProductDetails() {
      const productid = document.getElementById('prod_id').value;
      if (!productid) { alert("Enter Product ID!"); return; }
      callAPI("product-details/", "POST", { productid });
    }
    // ---------- DOCTOR FUNCTIONS ----------
    function getDoctorSchedule() {
      const doctorid = document.getElementById('doc_id').value;
      const mode = document.getElementById('doc_mode').value;
      if (!doctorid) { alert("Enter Doctor ID!"); return; }
      callAPI("doctor-schedule/", "POST", { doctorid, mode });
    }
    function submitDoctorFeedback() {
      const userid = document.getElementById('doc_feedback_userid').value;
      const prodid = document.getElementById('doc_feedback_prodid').value;
      const description = document.getElementById('doc_feedback_desc').value;
      const rating = document.getElementById('doc_feedback_rating').value;
      if (!userid || !prodid || !description || !rating) {
        alert("Fill all doctor feedback fields.");
        return;
      }
      callAPI("doctor-feedback/", "POST", { userid, prodid, description, rating });
    }
    function viewHealthRecords() {
      const userid = document.getElementById('health_userid').value;
      if (!userid) { alert("Enter Patient ID!"); return; }
      callAPI("health-records/", "POST", { userid });
    }
    function viewDoctorProfile() {
      const doctorid = document.getElementById('doc_profileid').value;
      if (!doctorid) { alert("Enter Doctor ID!"); return; }
      callAPI("doctor-profile/", "POST", { doctorid });
    }
    function updateDoctorRating() {
      const doctorid = document.getElementById('doc_upd_id').value;
      const new_rating = document.getElementById('doc_new_rating').value;
      if (!doctorid || !new_rating) { alert("Fill all fields for updating rating."); return; }
      callAPI("update-doctor-rating/", "POST", { doctorid, new_rating });
    }
    function getAppointmentsByDoctor() {
      const doctorid = document.getElementById('doc_id').value;
      if (!doctorid) { alert("Enter Doctor ID!"); return; }
      callAPI("appointments-by-doctor/", "POST", { doctorid });
    }
    function allDoctors() {
      callAPI("doctors/", "GET");
    }
    function filterDoctorsBySpecialization() {
      const specialization = document.getElementById('doc_specialization').value;
      if (!specialization) { alert("Select a specialization!"); return; }
      callAPI("doctors/filter/", "POST", { specialization });
    }
    function sortDoctorsByRating() {
      const spec = document.getElementById('doc_specialization').value;
      let endpoint = "doctors/sort/rating/";
      if (spec) { endpoint += "?specialization=" + encodeURIComponent(spec); }
      callAPI(endpoint, "GET");
    }
    function sortDoctorsByFee() {
      const spec = document.getElementById('doc_specialization').value;
      let endpoint = "doctors/sort/fee/";
      if (spec) { endpoint += "?specialization=" + encodeURIComponent(spec); }
      callAPI(endpoint, "GET");
    }
    function loadDoctorSpecializations() {
      fetch(API + "doctor-specializations/")
      .then(res => res.json())
      .then(data => {
         const sel = document.getElementById('doc_specialization');
         sel.innerHTML = '<option value="">--Select--</option>';
         data.forEach(spec => { sel.innerHTML += `<option value="${spec}">${spec}</option>`; });
      })
      .catch(err => console.error(err));
    }
    // ---------- ADMIN FUNCTIONS ----------
    function getHighValueCustomers() {
      callAPI("high-value-customers/", "GET");
    }
    function getPatientMedicalSummary() {
      callAPI("patient-medical-summary/", "GET");
    }
    function getUsersWithPrescriptionOrders() {
      callAPI("users-prescription-orders/", "GET");
    }
    function getUsersSpendingWithOffers() {
      callAPI("users-spending-with-offers/", "GET");
    }
    function viewAllUsers() { callAPI("all-users/", "GET"); }
    function addUser() {
      const name = document.getElementById('new_user_name').value;
      const email = document.getElementById('new_user_email').value;
      const phonenumber = document.getElementById('new_user_phone').value;
      const password = document.getElementById('new_user_password').value;
      callAPI("add-user/", "POST", { name, email, phonenumber, password });
    }
    function deleteUser() {
      const user_id = document.getElementById('adm_userid').value;
      if (!user_id) { alert("Enter User ID to delete."); return; }
      callAPI("delete-user/" + user_id + "/", "DELETE");
    }
    function addProduct() {
      const name = document.getElementById('new_prod_name').value;
      const brand = document.getElementById('new_prod_brand').value;
      const price = parseFloat(document.getElementById('new_prod_price').value);
      const composition = document.getElementById('new_prod_comp').value;
      const type = document.getElementById('new_prod_type').value;
      const prescriptionneeded = document.getElementById('new_prod_pres').checked;
      callAPI("add-product/", "POST", { name, brand, price, composition, type, prescriptionneeded });
    }
    function listDoctorsRatings() {
      callAPI("doctors-ratings/", "GET");
    }
    function updateProductPrice() {
      const product_id = document.getElementById('upd_prod_id').value;
      const new_price = parseFloat(document.getElementById('upd_prod_price').value);
      callAPI("update-product-price/", "POST", { product_id, new_price });
    }
    function getRecentActiveUsers() {
      callAPI("recent-active-users/", "GET");
    }
    function deleteProduct() {
      const product_id = document.getElementById('del_prod_id').value;
      if (!product_id) { alert("Enter Product ID to delete."); return; }
      callAPI("delete-product/" + product_id + "/", "DELETE");
    }
    function getMostOrderedProducts() { callAPI("most-ordered-products/", "GET"); }
    function addLabTest() {
      const name = document.getElementById('lab_name').value;
      const price = parseFloat(document.getElementById('lab_price').value);
      const status = document.getElementById('lab_status').value;
      const testdetails = document.getElementById('lab_details').value;
      callAPI("add-lab-test/", "POST", { name, price, status, testdetails });
    }
    function getUserOrderHistory() {
      callAPI("user-order-history/", "GET");
    }
    function getTopRevenueProductsForPrescriptionUsers() {
      callAPI("top-revenue-products-prescription-users/", "GET");
    }
    function getRecentDoctorStats() {
      callAPI("recent-doctor-appointments/", "GET");
    }
    function linkReport() {
      const userid = document.getElementById('cust_userid').value;
      const test_id = document.getElementById('rep_testid2').value;
      callAPI("link-report/", "POST", { userid, test_id });
    }
    function viewAllOffers() { callAPI("all-offers/", "GET"); }
    function sendNotification() {
      const user_id = document.getElementById('not_userid').value;
      const message = document.getElementById('not_message').value;
      const type = document.getElementById('not_type').value;
      callAPI("send-notification/", "POST", { user_id, message, type });
    }
    function findUsersFeedback() {
      callAPI("users-with-orders-feedback/", "GET");
    }
    function getHighestRatedDoctorsBySpecialization() {
      callAPI("highest-avg-rated-doctor/", "GET");
    }
    function getDoctorVisitCounts() {
      callAPI("doctors-total-visits/", "GET");
    }
    // Load doctor specializations on page load.
    window.onload = loadDoctorSpecializations;