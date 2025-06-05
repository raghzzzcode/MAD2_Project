<template>
  <div class="container-fluid mb-5">
    <AdminNavbar />
    <div class="row mt-4">
      <!-- Revenue from Each Parking Lot -->
      <div class="col-md-6">
        <div class="card custom-card shadow-lg border-0 rounded-3">
          <div class="card-body" style="min-height: 250px; padding: 1.5rem;">
            <h5 class="card-title mb-4 custom-heading">
              Revenue from Each Parking Lot
            </h5>
            <div class="d-flex justify-content-center">
              <canvas id="revenueChart" width="300" height="300"></canvas>
            </div>
          </div>
        </div>
      </div>

      <!-- Summary of Available and Occupied Lots -->
      <div class="col-md-6">
        <div class="card custom-card shadow-lg border-0 rounded-3">
          <div class="card-body" style="min-height: 250px; padding: 1.5rem;">
            <h5 class="card-title mb-4 custom-heading">
              Summary on Available and Occupied Parking Lots
            </h5>
            <div class="d-flex justify-content-center">
              <canvas id="occupancyChart" width="300" height="300"></canvas>
            </div>
          </div>
        </div>
      </div>
    </div>
    <AppFooter />
  </div>
</template>

<script>
import { onMounted } from 'vue';
import Chart from 'chart.js/auto';
import AdminNavbar from '@/components/AdminNavbar.vue';
import AppFooter from '@/components/AppFooter.vue';

export default {
  components: {
    AdminNavbar,
    AppFooter,
  },
  setup() {
    const revenueData = [
      { lot: 'Lot A', revenue: 12000 },
      { lot: 'Lot B', revenue: 8500 },
      { lot: 'Lot C', revenue: 14500 },
    ];

    const occupancySummary = {
      available: 37,
      occupied: 63,
    };

    const initCharts = () => {
      // Revenue Doughnut Chart
      const ctxRevenue = document.getElementById('revenueChart').getContext('2d');
      new Chart(ctxRevenue, {
        type: 'doughnut',
        data: {
          labels: revenueData.map((r) => r.lot),
          datasets: [{
            data: revenueData.map((r) => r.revenue),
            backgroundColor: ['#5c6bc0', '#42a5f5', '#ffb74d'],
            borderColor: '#ffffff',
            borderWidth: 2,
          }],
        },
        options: {
          plugins: {
            legend: {
              position: 'top',
              labels: { color: '#ffffff' },
            },
            tooltip: {
              callbacks: {
                label: (tooltipItem) => `₹${tooltipItem.raw.toLocaleString()} revenue`,
              },
              backgroundColor: '#222',
              titleColor: '#fff',
              bodyColor: '#fff',
            },
          },
          maintainAspectRatio: false,
        },
      });

      // Occupancy Bar Chart
      const ctxOccupancy = document.getElementById('occupancyChart').getContext('2d');
      new Chart(ctxOccupancy, {
        type: 'bar',
        data: {
          labels: ['Available', 'Occupied'],
          datasets: [{
            label: 'Parking Slots',
            data: [occupancySummary.available, occupancySummary.occupied],
            backgroundColor: ['#81c784', '#e57373'],
            borderColor: '#ffffff',
            borderWidth: 2,
          }],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
              ticks: { color: '#ffffff' },
              grid: {
                color: 'rgba(255,255,255,0.2)',
              },
            },
            x: {
              ticks: { color: '#ffffff' },
              grid: {
                color: 'rgba(255,255,255,0.2)',
              },
            },
          },
          plugins: {
            legend: {
              display: false,
              labels: { color: '#ffffff' },
            },
            tooltip: {
              callbacks: {
                label: (tooltipItem) => `${tooltipItem.label}: ${tooltipItem.raw} slots`,
              },
              backgroundColor: '#222',
              titleColor: '#fff',
              bodyColor: '#fff',
            },
          },
          maintainAspectRatio: false,
        },
      });
    };

    onMounted(() => {
      initCharts();
    });
  },
};
</script>

<style scoped>
.custom-card {
  background-color:rgb(5, 28, 65); /* subtle light blue background */
}

.custom-heading {
  color:rgb(150, 190, 242);
  font-weight: 600;
  font-size: 1.5rem;
}

canvas {
  width: 100% !important;
  height: 300px !important;
}
</style>
