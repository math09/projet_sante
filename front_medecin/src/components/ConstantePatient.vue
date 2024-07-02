<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'
import PrimaryButton from '@/components/PrimaryButton.vue';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement)


export default {
  components: {
    PrimaryButton,
    Line
  },
  // props:{
  //   examens: {
  //     type: Array,
  //     required: true
  //   },
  //   chartData: {
  //     type: Object,
  //     required: true
  //   },
  //   chartOptions: {
  //     type: Object,
  //     default: () => {}
  //   }
  // },
  data() {
    return {
      chartData: {
        labels: ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet"],
        datasets: [{
          label: 'My First Dataset',
          data: [65, 59, 80, 81, 56, 55, 40],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-2">
        
      <div class="col-span-1 row-span-3 p-2 bg-white rounded-md">
        <div class="rounded-3xl">
          <div class="flex w-full">
            Dernière constante
          </div>
        </div>
      </div>
    
      <div class="col-span-4 row-span-5 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div class="flex flex-col h-full gap-4 p-2 overflow-auto">Test
          <Line id="my-chart-id" :options="chartOptions" :data="chartData"/>
        </div>
      </div>

      <div class="col-span-1 row-span-2 p-2 bg-white rounded-md">
        <div class="rounded-3xl">
          <h2>Nouvelle constante</h2>
          <div class="">
            <PrimaryButton v-for="(examen, index) in examens" :key="index" class='mb-2'>{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
          </div>
        </div>
      </div>

      

    </div>
  </BaseLayout>
</template>
