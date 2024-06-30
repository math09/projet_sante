<template>
  <div class="grid h-full rounded-3xl">
    <div class="flex w-full grid-rows-1 ">
    <InputComponent id="search" label="Rechercher" type="text" v-model="search" @input-c="searchInDb" input-class="w-full h-4 border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
      <SearchIcon/>
    </InputComponent>
    </div>
    
    <div class="flex-grow grid-rows-2 overflow-auto pb-52">
      <PrimaryButton v-for="(person, index) in persons" :key="index" class='mb-2'>{{ person.nom }} {{ person.prenom }}</PrimaryButton>
    </div>
  </div>
  
</template>

<script>
import InputComponent from '@/components/InputComponent.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import PrimaryButton from './PrimaryButton.vue';

export default {
  components: {
    PrimaryButton,
    InputComponent,
    SearchIcon,
  },
  props: {
    persons: {
      type: Array,
      required: true
    }
  }
};
</script>