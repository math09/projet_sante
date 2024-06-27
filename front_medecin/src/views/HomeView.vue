<script>
import BaseLayout from '@/layouts/BaseLayout.vue';
import InputComponent from '@/components/InputComponent.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import InfoComponent from '@/components/InfoComponent.vue';
import ListPatient from '@/components/ListPatient.vue';

export default {
  name: 'HomeView',
  components: {
    BaseLayout,
    InputComponent,
    PrimaryButton,
    SearchIcon,
    InfoComponent,
    ListPatient
  },
  data() {
    return {
      persons: [
        { id: 1, nom: "JEAN", prenom: "Anthony", age: "11/05/2003 (20 ans)", num_secu: "1 03 59 034 456" },
        { id: 2, nom: "SMITH", prenom: "John", age: "10/05/2003 (25 ans)", num_secu: "1 02 38 932 678" },
      ],
      page: 1
    };
  },
  methods: {
    navBarre(index){
      console.log(index);
      this.page = index
      console.log(this.page);
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-8">
        
          <div class="flex-grow">
            <ListPatient :persons="persons" :selected-row="selectedRow" @row-selected="onRowSelected"/>
          </div>

     <!--  <div class="h-full overflow-auto ">
        <InfoComponent :data="persons[selectedRow]" @update:modify="modifyInfo = true" :modify="modifyInfo" :create="createMode"/>
      </div> -->

      <div class="col-span-4 overflow-hidden bg-gradient-to-tr">
        <div class="flex flex-col h-full">
          <div class="flex items-end justify-between">
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(1)" :buttonClass="{'bg-white bg-image-none text-black':page!=1}">Informations patient</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(2)" :buttonClass="{'bg-white bg-image-none text-black':page!=2}">Examens</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(3)" :buttonClass="{'bg-white bg-image-none text-black':page!=3}">Constante</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(4)" :buttonClass="{'bg-white bg-image-none text-black':page!=4}">Prescription</PrimaryButton>
          </div>
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
