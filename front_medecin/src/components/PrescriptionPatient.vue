<!-- eslint-disable vue/no-mutating-props -->
<script>
import InputComponent from '@/components/InputComponent.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';

export default {
  components: {
    InputComponent,
    SearchIcon,
    PrimaryButton
  },
  props:{
    examens: {
      type: Array,
      required: true
    }
  },
  data(){
    return {
      medicSelected: 0
    }
  },
  methods:{
    selectedMedicament(id){
      if (id == this.medicSelected) this.medicSelected=0;
      else this.medicSelected=id;
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-2">
        
          <div class="flex-grow p-2 bg-white rounded-md">
            <div class="grid h-full rounded-3xl">
              <div class="flex w-full grid-rows-1 ">
              <InputComponent id="search" label="Rechercher" type="text" v-model="search" @input-c="searchInDb" input-class="w-full h-4 border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
                <SearchIcon/>
              </InputComponent>
              </div>
              
              <div class="flex-grow grid-rows-2 overflow-auto pb-52">
                <PrimaryButton v-for="(medicament, index) in medicament" :key="index" @click="selectedMedicament(examen.id_examen)" class='mb-2'>{{ medicament.nom }} <br> {{ medicament.molecule }} <br> {{ medicament.ref }}</PrimaryButton>
              </div>
            </div>
          </div>

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div @update:examSelected="examen.id_examen" class="flex flex-col h-full col-span-3 gap-6 p-2">
        
        <div class="grid w-full h-full grid-rows-3 gap-2">
          <div class="w-full h-full row-span-1 pb-5">
            <div>Médicament sélctionné :</div>
            <div class="w-full h-full grid-cols-3">
              <div class="w-full h-full col-span-1">
              </div>
              <div class="w-full h-full col-span-2">
                <p>Date de début : <input class="bg-mercury-200" type="text"></p>
              </div>
              <div class="w-full h-full col-span-3"></div>
              <div class="w-full h-full col-span-3"></div>
            </div>
          </div>
          <div class="w-full h-full row-span-2 pb-5">
            <div>Champs libre :</div>
            <textarea style="resize: none;" class="w-full h-full rounded-md bg-mercury-200" name="diagnostic"></textarea>
          </div>
          <div class="w-full h-full row-span-3 pb-5">
            <div>Signature :</div>
            <textarea style="resize: none;" class="w-full h-full rounded-md bg-mercury-200" name="resultat"></textarea>
          </div>
        </div>
          
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
