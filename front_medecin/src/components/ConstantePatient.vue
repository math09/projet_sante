<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import PrimaryButton from '@/components/PrimaryButton.vue';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


export default {
  components: {
    PrimaryButton,
    Bar
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
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
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
        
      <!-- <div class="flex-grow p-2 bg-white rounded-md">
        <div class="grid h-[2/3] rounded-3xl">
          <div class="flex w-full grid-rows-1 ">
            dernière constante
          </div>
        </div>
      </div>
    
      <div class="flex-grow p-2 bg-white rounded-md">
        <div class="grid h-[1/3] rounded-3xl">
          <div class="flex w-full grid-rows-1 ">
          </div>
            Nouvelle constante
          <div class="flex-grow grid-rows-2 pb-52">
            <PrimaryButton v-for="(examen, index) in examens" :key="index" class='mb-2'>{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
          </div>
        </div>
      </div> -->

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div class="flex flex-col h-full gap-4 p-2 overflow-auto">Test
          <Bar id="my-chart-id" :options="chartOptions" :data="chartData"/>
        </div>
      </div>

    </div>
  </BaseLayout>
</template>
