<template>
  <div>
    <!-- Include Navbar -->
    <AppNavbar />

    <!-- Main content area -->
    <div class="container my-5 main-wrapper">
      <h1 class="text-center main-heading">🚦 Welcome to ParkEase</h1>
      <p class="text-center subheading">Seamless and smart vehicle parking management at your fingertips</p>

      <div class="row justify-content-center text-center mt-4">
        <div class="col-md-4 mb-4">
          <div class="card custom-card">
            <img src="@/assets/customer.jpeg" alt="Customer" class="img-fluid uniform-image">
            <div class="card-body">
              <router-link to="/alllogin" class="btn btn-lg custom-btn red-light-btn">
                <i class="fas fa-user"></i> Customer Login
              </router-link>
              <p class="text-muted mt-2">Reserve parking slots with ease</p>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-4">
          <div class="card custom-card">
            <img src="@/assets/admin.png" alt="Admin" class="img-fluid uniform-image">
            <div class="card-body">
              <router-link to="/alllogin" class="btn btn-lg custom-btn red-light-btn">
                <i class="fas fa-cog"></i> Admin Login
              </router-link>
              <p class="text-muted mt-2">Monitor and manage the platform</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Include Footer -->
    <AppFooter />
  </div>
</template>

<script>
import AppNavbar from '@/components/AppNavbar.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  name: 'BaseLayout',
  components: {
    AppNavbar,
    AppFooter
  }
}
</script>

<style scoped>
body {
  background: linear-gradient(to bottom right, #dbe9ff, #aacdff);
  font-family: 'Helvetica Neue', sans-serif;
  line-height: 1.6;
}

/* Road-style content wrapper */
.main-wrapper {
  min-height: calc(100vh - 150px);
  background: repeating-linear-gradient(
    to bottom,
    #1a2238, /* deep navy */
    #1a2238 40px,
    #283655 40px,
    #283655 45px
  );
  border-radius: 20px;
  box-shadow: 0 6px 25px rgba(0, 0, 0, 0.3);
  padding: 30px;
  border: 3px dashed #3a5fcd; /* bluish border */
  transition: all 0.3s ease;
  position: relative;
  color: #e0e6f0; /* lighter text for dark bg */
}

/* Dashed line strip at bottom to mimic a road lane */
.main-wrapper::after {
  content: '';
  display: block;
  height: 6px;
  width: 100%;
  background-image: repeating-linear-gradient(
    to right,
    #3a5fcd 0,
    #3a5fcd 30px,
    transparent 30px,
    transparent 60px
  );
  margin-top: 40px;
}

.main-heading {
  color: #64b5f6; /* lighter blue */
  font-weight: 800;
  margin-bottom: 25px;
  font-size: 2.2rem;
}

.subheading {
  color: #cfd8dc; /* light grey */
  font-size: 1.2rem;
}

.custom-card {
  background: #202c4a; /* dark bluish card */
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  border: 2px solid #3a5fcd; /* bluish border */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  color: #e0e6f0;
}
.card-body p {
  color: #ffffff !important;
}


.custom-card:hover {
  transform: translateY(-7px);
  box-shadow: 0 12px 30px rgba(58, 95, 205, 0.8);
}

.uniform-image {
  height: 170px;
  object-fit: cover;
  width: 100%;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.custom-btn {
  border-radius: 30px;
  font-size: 1.1rem;
  padding: 10px 25px;
  border: none;
  background-color: #0d47a1; /* vehicle blue */
  border: 1px dashed #64b5f6;
  color: #fff;
  transition: background-color 0.3s ease;
  cursor: pointer;
}

.custom-btn:hover {
  background-color: #1565c0;
  color: #fff;
}

p {
  color: #cfd8dc;
}

h1, h2, h3, h4, h5, h6 {
  color: #64b5f6;
}

</style>


