<template>
<!-- Navbar Component -->
    <CustomerNavbar />
  <div class="release-container">
    <!-- Heading -->
    <h2 class="release-title">Release the parking spot</h2>

    <!-- Release Form -->
    <form @submit.prevent="submitRelease" class="release-form">
      <!-- Pre-filled Fields -->
      <div class="form-group">
        <label for="spotId">Spot ID:</label>
        <input type="text" id="spotId" v-model="form.spotId" readonly />
      </div>

      <div class="form-group">
        <label for="vehicleNumber">Vehicle Number:</label>
        <input type="text" id="vehicleNumber" v-model="form.vehicleNumber" readonly />
      </div>

      <div class="form-group">
        <label for="parkingTime">Parking Time:</label>
        <input type="text" id="parkingTime" v-model="form.parkingTime" readonly />
      </div>

      <div class="form-group">
        <label for="releasingTime">Releasing Time:</label>
        <input type="text" id="releasingTime" v-model="form.releasingTime" readonly />
      </div>

      <div class="form-group">
        <label for="totalCost">Total Cost:</label>
        <input type="text" id="totalCost" v-model="form.totalCost" readonly />
      </div>

      <!-- Buttons -->
      <div class="button-group">
        <button type="submit" class="btn release">Release</button>
        <button type="button" class="btn cancel" @click="cancelRelease">Cancel</button>
      </div>
    </form>
  </div>
  <AppFooter />
</template>

<script>
import CustomerNavbar from "@/components/CustomerNavbar.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  name: 'CustomerRelease',
  components: {
    CustomerNavbar,
    AppFooter
  },
  props: {
    spotId: String,
    vehicleNumber: String,
    parkingTime: String,
    releasingTime: String,
    totalCost: String
  },
  data() {
    return {
      form: {
        spotId: this.spotId || 'SP456',
        vehicleNumber: this.vehicleNumber || 'MH12AB1234',
        parkingTime: this.parkingTime || '2025-06-04 09:00',
        releasingTime: this.releasingTime || new Date().toISOString().slice(0, 16).replace('T', ' '),
        totalCost: this.totalCost || '₹100'
      }
    };
  },
  methods: {
    submitRelease() {
      console.log("Parking spot released:", this.form);
      alert("Parking spot successfully released!");
    },
    cancelRelease() {
      alert("Cancelled releasing the spot.");
    }
  }
};
</script>


<style scoped>
.release-container {
  max-width: 460px;
  margin: 3rem auto;
  padding: 2rem 2.5rem;
  background: #202c4a; /* dark blue background */
  border-radius: 20px;
  border: 2px solid #3a5fcd; /* consistent blue border */
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.3);
  color: #e0e6f0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  user-select: none;
}

.release-title {
  background-color: #283655; /* dark header blue */
  padding: 1rem 0;
  border-radius: 20px;
  text-align: center;
  font-size: 1.8rem;
  font-weight: 800;
  color: #64b5f6;
  margin-bottom: 2rem;
  box-shadow: 0 4px 10px rgba(58, 95, 205, 0.6);
}

.release-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.4rem;
}

label {
  flex: 1;
  font-weight: 700;
  color: #64b5f6;
  font-size: 1.1rem;
}

input {
  flex: 2;
  padding: 0.5rem 0.75rem;
  border: 2px solid #3a5fcd;
  border-radius: 12px;
  font-size: 1rem;
  color: #202c4a; /* dark text for readability */
  background-color: #e0e6f0; /* light input background */
  transition: border-color 0.3s ease;
  user-select: text;
}

input:focus {
  outline: none;
  border-color: #64b5f6;
  box-shadow: 0 0 8px #64b5f6;
}

input[readonly] {
  background-color: #283655;
  color: #9bb9e8;
  font-style: italic;
  user-select: none;
  border-color: #283655;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-top: 2rem;
}

.btn {
  padding: 0.65rem 2.4rem;
  font-weight: 700;
  font-size: 1.1rem;
  border-radius: 30px;
  border: 2px solid transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  user-select: none;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.release {
  background-color: #3a5fcd;
  color: #e0e6f0;
  border-color: #64b5f6;
}

.release:hover {
  background-color: #64b5f6;
  color: #202c4a;
  border-color: #3a5fcd;
  box-shadow: 0 0 15px #64b5f6;
}

.cancel {
  background-color: transparent;
  color: #ef5350;
  border: 2px solid #ef5350;
}

.cancel:hover {
  background-color: #ef5350;
  color: #fff;
  box-shadow: 0 0 15px #ef5350;
}

</style>
