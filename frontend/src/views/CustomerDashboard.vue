<template>
  <div>
    <!-- Customer Navbar -->
    <CustomerNavbar />

    <div class="container-fluid mt-4 mb-5">
      <h4 class="section-title">Recent Parking History</h4>
      <table class="table table-bordered table-striped shadow table-dark table-hover">
        <thead>
          <tr>
            <th>Parking Lot ID</th>
            <th>Parking Spot ID</th>
            <th>Parking Lot Address</th>
            <th>Parking Timestamp</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="entry in parkingHistory" :key="entry.id">
            <td>{{ entry.parking_lot_id }}</td>
            <td>{{ entry.parking_spot_id }}</td>
            <td>{{ entry.address }}</td>
            <td>{{ entry.parking_timestamp }}</td>
            <td>{{ entry.timestamp }}</td>
            <td>
              <button
                v-if="entry.status === 'O'"
                class="btn btn-danger btn-sm"
                @click="releaseParking"
              >
                Release
              </button>
              <span v-else class="badge bg-success">Parked Out</span>
            </td>
          </tr>
        </tbody>
      </table>

      <div class="text-center my-4">
        <label for="locationSearch" class="form-label fs-5">Search parking @location/pin code:</label>
        <input
          type="text"
          id="locationSearch"
          class="form-control w-50 mx-auto"
          v-model="searchLocation"
          placeholder="e.g. Dadar Road"
          @keyup.enter="searchParkingLots"
        />
      </div>

      <div v-if="parkingLots.length > 0">
        <h4 class="section-title">Parking Lots @ {{ searchLocation }}</h4>
        <table class="table table-dark table-hover shadow rounded">
          <thead>
            <tr>
              <th>Parking Lot ID</th>
              <th>Parking Spot ID</th>
              <th>Address</th>
              <th>Availability</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lot in parkingLots" :key="lot.id">
              <td>{{ lot.parking_lot_id }}</td>
              <td>{{ lot.parking_spot_id }}</td>
              <td>{{ lot.address }}</td>
              <td>{{ lot.availability }}</td>
              <td>
                <button class="btn btn-primary btn-sm" @click="bookParking">
                  Book
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="text-center text-muted">
        <p>No parking lots found. Try searching a location.</p>
      </div>
    </div>

    <!-- App Footer -->
    <AppFooter />
  </div>
</template>

<script>
import CustomerNavbar from "@/components/CustomerNavbar.vue";
import AppFooter from "@/components/AppFooter.vue";


export default {
  components: {
    CustomerNavbar,
    AppFooter,
  },
  data() {
    return {
      parkingHistory: [],
      searchLocation: "",
      parkingLots: [],
      dummyLots: [
        { parkind_spot_id: 1, address: "Dadar West", availability: "A" },
        { parkind_spot_id: 2, address: "Andheri East", availability: "O" },
        { parkind_spot_id: 3, address: "Bandra Station", availability: "A" },
      ],
    };
  },
  methods: {
    getCustomerEmail() {
      return "test@example.com"; // Replace with actual logic later
    },

    fetchParkingHistory() {
      this.parkingHistory = [
        {
          id: 101,
          location: "Dadar West",
          vehicle_no: "MH12AB1234",
          timestamp: "2025-06-04 10:15:00",
          status: "active",
        },
        {
          id: 102,
          location: "Andheri East",
          vehicle_no: "MH01XY7890",
          timestamp: "2025-06-03 18:45:00",
          status: "released",
        },
      ];
    },

    searchParkingLots() {
      this.parkingLots = this.dummyLots.filter((lot) =>
        lot.address.toLowerCase().includes(this.searchLocation.toLowerCase())
      );
    },

    async bookParking() {
     this.$router.push('/customer_booking');
    },

    async releaseParking() {
      this.$router.push('/customer_releasing');
    },
  },
  mounted() {
    this.fetchParkingHistory();
  },
};
</script>



<style scoped>
/* Background and container */
.container-fluid {
  background-color: #1a2238; /* dark navy */
  padding: 2rem;
  border-radius: 20px;
  color: #e0e6f0; /* light text */
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.3);
  min-height: calc(100vh - 150px);
  border: 3px dashed #3a5fcd; /* bright blue border */
  transition: all 0.3s ease;
}

/* Section Titles */
.section-title {
  color: #64b5f6; /* bright blue */
  font-weight: 800;
  font-size: 2rem;
  text-align: center;
  margin-bottom: 1.5rem;
}

/* Table */
.table {
  background-color: #202c4a; /* card blue */
  color: #e0e6f0;
  border: 2px solid #3a5fcd;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
  overflow: hidden;
}

.table th {
  background-color: #283655; /* slightly lighter background for header */
  color: #64b5f6;
  font-weight: 700;
  text-align: center;
  border-bottom: 2px solid #3a5fcd;
}

.table td {
  text-align: center;
  border-top: 1px solid #3a5fcd;
  vertical-align: middle;
  font-weight: 600;
}

/* Table hover */
.table-hover tbody tr:hover {
  background-color: #3a5fcd33; /* translucent bright blue */
  cursor: pointer;
}

/* Buttons */
.btn-primary {
  background-color: #3a5fcd;
  border: 1px solid #64b5f6;
  color: #e0e6f0;
  font-weight: 700;
  border-radius: 30px;
  padding: 5px 15px;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #64b5f6;
  border-color: #3a5fcd;
  color: white;
}

.btn-danger {
  background-color: #e53935;
  border: 1px solid #ef5350;
  color: white;
  font-weight: 700;
  border-radius: 30px;
  padding: 5px 15px;
  transition: background-color 0.3s ease;
}

.btn-danger:hover {
  background-color: #ef5350;
  border-color: #e53935;
  color: white;
}

/* Badge */
.badge.bg-success {
  background-color: #4caf50;
  font-weight: 700;
  font-size: 0.9rem;
  padding: 0.5em 0.8em;
  border-radius: 12px;
  color: white;
}

/* Input */
.form-control {
  background-color: #202c4a;
  color: #e0e6f0;
  border: 2px solid #3a5fcd;
  border-radius: 12px;
  font-weight: 600;
  max-width: 500px;
  margin: 0 auto;
  display: block;
  transition: border-color 0.3s ease;
}

.form-control::placeholder {
  color: #64b5f6;
  opacity: 0.7;
}

.form-control:focus {
  outline: none;
  border-color: #64b5f6;
  box-shadow: 0 0 8px #64b5f6aa;
}

/* Centered label */
label.form-label {
  color: #64b5f6;
  font-weight: 700;
  text-align: center;
  display: block;
  margin-bottom: 0.75rem;
}

/* Text-muted fallback */
.text-muted {
  color: #9e9e9e !important;
  font-style: italic;
  margin-top: 1rem;
  font-weight: 500;
}

/* Responsive tweaks */
@media (max-width: 768px) {
  .form-control {
    width: 90% !important;
  }
}
</style>

