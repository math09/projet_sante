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
      examSelected: null
    }
  },
  methods:{
    selectedExamen(id){
      if (id == this.examSelected) this.examSelected=null;
      else this.examSelected=id;
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
                <PrimaryButton v-for="(examen, index) in examens" :key="index" @click="selectedExamen(examen.id_examen)" class='mb-2'>{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
              </div>
            </div>
          </div>

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div class="flex flex-col h-full col-span-3 gap-6 p-2">
        
          <div v-if="this.examSelected!=null" class="grid w-full h-full grid-cols-3 gap-2">
            <div class="w-full h-full col-span-2 row-span-1 pb-5">
              <div>Motif :</div>
              <p class="w-full h-full bg-mercury-200">{{ examens.find(examen => examen.id_examen==examSelected).motif }}</p>
            </div>
            <div class="w-full h-full col-span-1 row-span-3 pb-5">
              <div>Diagnostic :</div>
              <p class="w-full h-full bg-mercury-200">{{ examens.find(examen => examen.id_examen==examSelected).diagnostic }}</p>
            </div>
            <div class="w-full h-full col-span-2 row-span-2 pb-5">
              <div>Résultats d'analyse :</div>
              <p class="w-full h-full bg-mercury-200">{{ examens.find(examen => examen.id_examen==examSelected).resultat_analyse }}</p>
            </div>
            <div class="w-full h-full col-span-2 row-span-2 pb-5">
              <div class="w-full h-fit">Conclusion :</div>
              <p class="w-full h-full bg-mercury-200">{{ examens.find(examen => examen.id_examen==examSelected).conclusion }}</p>
            </div>
            <div class="w-full h-full col-span-1 row-span-2 pb-5">
              <div>Observation :</div>
              <p class="w-full h-full bg-mercury-200">{{ examens.find(examen => examen.id_examen==examSelected).observation }}</p>
            </div>
          </div>
        
          <div v-else>
            <div class="flex justify-end"><PrimaryButton class="text-white w-fit px-14">Valider</PrimaryButton></div>
            <div class="grid w-full h-full grid-cols-3 gap-2">
              <div class="w-full h-full col-span-2 row-span-1 pb-5">
                <div class="w-full h-fit">Motif :</div>
                <textarea style="resize: none;" class="w-full h-full bg-mercury-200" name="motif"></textarea>
              </div>
              <div class="w-full h-full col-span-1 row-span-3 pb-5">
                <div class="w-full h-fit">Diagnostic :</div>
                <textarea style="resize: none;" class="w-full h-full bg-mercury-200" name="diagnostic"></textarea>
              </div>
              <div class="w-full h-full col-span-2 row-span-2 pb-5">
                <div class="w-full h-fit">Résultats d'analyse :</div>
                <textarea style="resize: none;" class="w-full h-full bg-mercury-200" name="resultat"></textarea>
              </div>
              <div class="w-full h-full col-span-2 row-span-2 pb-5">
                <div class="w-full h-fit">Conclusion :</div>
                <textarea style="resize: none;" class="w-full h-full bg-mercury-200" name="conclusion"></textarea>
              </div>
              <div class="w-full h-full col-span-1 row-span-2 pb-5">
                <div class="relative w-full h-fit">Observation :</div>
                <textarea style="resize: none;" class="w-full h-full bg-mercury-200" name="observation"></textarea>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
