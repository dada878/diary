<template>
    <GlassWindowEffect>
        <!-- <PieChart :chartData="data" /> -->
    </GlassWindowEffect>
</template>
  
<script lang="ts">
import { defineComponent } from 'vue';
// import { PieChart } from 'vue-chart-3';
// import { Chart, registerables } from "chart.js";
import GlassWindowEffect from './GlassWindowEffect.vue';

// Chart.register(...registerables);

export default defineComponent({
    components: { GlassWindowEffect },
//     setup() {
//         const data = {
//             labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//             datasets: [{
//                 label: '# of Votes',
//                 data: [12, 19, 3, 5, 2, 3],
//                 borderWidth: 1,
//                 backgroundColor: ['#CB4335', '#1F618D', '#F1C40F', '#27AE60', '#884EA0', '#D35400'],
//             }]
//         };
//         return { data };
//     },
});
</script>