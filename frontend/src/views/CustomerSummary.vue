<template>
  <div>
    <!-- Navbar Component -->
    <CustomerNavbar />

    <div class="container-fluid my-5">
      <div class="row justify-content-center">
        <!-- Summary Chart Box -->
        <div class="col-md-4">
          <div class="summary-box">
            <div class="chart-container">
              <canvas id="serviceHistoryChart"></canvas>
            </div>
            <p class="chart-caption">Summary on already used parking spots</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer Component -->
    <AppFooter />
  </div>
</template>

<script>
import instance from '@/axios.js';
import Chart from 'chart.js/auto';
import CustomerNavbar from "@/components/CustomerNavbar.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  components: {
    CustomerNavbar,
    AppFooter
  },
  data() {
    return {
      serviceHistoryData: {
        Requested: 0,
        Assigned: 0,
        Closed: 0
      },
      customerEmail: localStorage.getItem('customer_email'),
      chartInstance: null
    };
  },
  mounted() {
    this.fetchServiceHistory();
  },
  methods: {
    fetchServiceHistory() {
      instance.get(`service-history/${this.customerEmail}`)
        .then(response => {
          this.serviceHistoryData = response.data;

          // Wait until DOM is ready to render the chart
          this.$nextTick(() => {
            this.createServiceHistoryChart();
          });
        })
        .catch(error => {
          console.error("Error fetching service history:", error);

          // Use fallback data if API fails
          this.serviceHistoryData = {
            Requested: 3,
            Assigned: 6,
            Closed: 4
          };

          this.$nextTick(() => {
            this.createServiceHistoryChart();
          });
        });
    },

    createServiceHistoryChart() {
      const ctx = document.getElementById('serviceHistoryChart').getContext('2d');
      if (this.chartInstance) {
        this.chartInstance.destroy();
      }

      this.chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Parking#1', 'Parking#2', 'Parking#3 '],
          datasets: [{
            label: 'Parking Stats',
            data: [
              this.serviceHistoryData.Requested,
              this.serviceHistoryData.Assigned,
              this.serviceHistoryData.Closed
            ],
            backgroundColor: ['#4A90E2', '#357ABD', '#2C5AA0'],
            borderRadius: 8,
            borderSkipped: false,
            borderWidth: 1
          }]
        },
        options: {
          responsive: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#004aad',
              callbacks: {
                label: tooltipItem => `${tooltipItem.label}: ${tooltipItem.raw}`
              }
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                stepSize: 1,
                font: {
                  size: 12,
                  weight: 'bold'
                }
              },
              grid: {
                drawBorder: false,
                color: '#eee'
              }
            },
            x: {
              ticks: {
                font: {
                  size: 12,
                  weight: 'bold'
                }
              },
              grid: {
                display: false
              }
            }
          }
        }
      });

      console.log("Chart created with:", this.serviceHistoryData);
    }
  }
};
</script>

<style scoped>
/* Container and overall layout */
.container-fluid.my-5 {
  background-color: #f8f9fa; /* light subtle gray background */
  padding: 2rem 1rem;
  min-height: 350px;
  border-radius: 1rem;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

/* Summary Box with soft shadows and rounded corners */
.summary-box {
  background: #ffffff;
  border-radius: 1.5rem;
  padding: 1.5rem 2rem;
  text-align: center;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.07);
  max-width: 360px;
  margin: 0 auto;
  transition: transform 0.3s ease;
}
.summary-box:hover {
  transform: translateY(-6px);
}

/* Chart Container - centered flexbox */
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 260px;
}

/* Canvas with fixed size and smooth edges */
canvas {
  width: 320px !important;
  height: 260px !important;
  border-radius: 1rem;
}

/* Caption below the chart with subtle styling */
.chart-caption {
  font-size: 1rem;
  margin-top: 1rem;
  color: #555555;
  font-style: italic;
  font-weight: 500;
  user-select: none;
  letter-spacing: 0.02em;
}

/* Responsive tweaks */
@media (max-width: 576px) {
  .summary-box {
    max-width: 100%;
    padding: 1rem;
  }
  canvas {
    width: 100% !important;
    height: 220px !important;
  }
}
</style>
