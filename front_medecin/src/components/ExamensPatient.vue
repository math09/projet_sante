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
                <PrimaryButton v-for="(examen, index) in examens" :key="index" class='mb-2'>{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
              </div>
            </div>
          </div>

      <div class="col-span-4 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div class="flex flex-col h-full gap-4 p-2">
          
          
          
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
