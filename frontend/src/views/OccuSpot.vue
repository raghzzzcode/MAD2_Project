<template>
  <div>
    <!-- Admin Navbar -->
    <AdminNavbar />

    <div class="container-fluid mb-5">
      <h3 class="text-center mb-4">Occupied Parking Spot Details</h3>

      <!-- Parking Spot Details -->
      <div class="mb-3">
        <label class="form-label fw-bold">ID:</label>
        <input type="text" class="form-control" v-model="spot.id" readonly />
      </div>

      <div class="mb-3">
        <label class="form-label fw-bold">Customer ID:</label>
        <input type="text" class="form-control" v-model="spot.customerId" readonly />
      </div>

      <div class="mb-3">
        <label class="form-label fw-bold">Vehicle Number:</label>
        <input type="text" class="form-control" v-model="spot.vehicleNumber" readonly />
      </div>

      <div class="mb-3">
        <label class="form-label fw-bold">Date/Time of Parking:</label>
        <input type="text" class="form-control" v-model="spot.parkingTime" readonly />
      </div>

      <div class="mb-3">
        <label class="form-label fw-bold">Estimated Parking Cost:</label>
        <input type="text" class="form-control" v-model="spot.estimatedCost" readonly />
      </div>

      <!-- Action Button -->
      <div class="text-end">
        <button class="btn btn-secondary btn-lg" @click="$router.push('/admin_dashboard')">
          Close
        </button>
      </div>
    </div>

    <!-- App Footer -->
    <AppFooter />
  </div>
</template>

<script>
import AdminNavbar from '@/components/AdminNavbar.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  name: 'OccuSpot',
  components: {
    AdminNavbar,
    AppFooter
  },
  data() {
    return {
      spot: {
        id: '1',
        customerId: 'CUST1234',
        vehicleNumber: 'MH12AB1234',
        parkingTime: '2025-06-04 10:00 AM',
        estimatedCost: '₹120.00'
      }
    };
  }
};
</script>

<style scoped>
body {
  background-color: #0d1b2a;
  color: #ffffff;
}

.container-fluid {
  max-width: 600px;
  padding: 2rem;
  background-color: #051c41;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.7);
  color: #ffffff;
}

.text-center {
  font-weight: bold;
  color: #bbdefb;
}

.form-label {
  color: #e0e0e0;
}

.form-control {
  background-color: #0a2855;
  color: #e3f2fd;
  border: 1px solid #2196f3;
}

.form-control:read-only {
  background-color: #102c4d;
}

.btn-secondary {
  width: 150px;
  background-color: #607d8b;
  border-color: #607d8b;
  color: #fff;
}

.btn-secondary:hover {
  background-color: #78909c;
  border-color: #78909c;
}
</style>
