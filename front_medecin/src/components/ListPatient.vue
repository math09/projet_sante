<template>
  <div class="h-full p-5 rounded-3xl bg-white">
    <div class="w-full gap-5">
      <InputComponent id="search" label="Rechercher" type="text" v-model="search" @input-c="searchInDb" input-class="w-full h-4 border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
        <SearchIcon/>
      </InputComponent>
    </div>
    
    <div class="flex flex-col gap-1 mt-10 overflow-auto">
      <PrimaryButton v-for="person in persons" :key="person.id" class='mb-2 py-1' @click="selectPerson(person.id)" :buttonClass="{'bg-neutral-200 bg-image-none text-black !shadow-none':personSelected!=person.id, 'text-white !shadow-none':personSelected==person.id}">{{ person.nom }} {{ person.prenom }}</PrimaryButton>
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
  },
  data() {
    return {
      personSelected: 5
    }
  },
  methods:{
    selectPerson(index){
      this.personSelected=index;
      this.$emit('person_selected',index)
    }
  }
};
</script>