<template>
  <div class="flex h-full p-5 bg-white rounded-3xl">
    <InputComponent id="search" label="Rechercher" type="text" class="w-[25%]" v-model="search" @input-c="searchInDb" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300">
      <SearchIcon/>
    </InputComponent>
        
    <div class="flex-grow overflow-auto">
      <PrimaryButton :persons="persons" :selected-row="selectedRow" @row-selected="onRowSelected"/>
    </div>
  </div>
  
</template>

<script>
import InputComponent from '@/components/InputComponent.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';

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
    },
    selectedRow: {
      type: Number,
      required: true
    }
  },
  methods: {
    isLastRow(index, length) {
      return index === length - 1;
    },
    selectRow(index) {
      this.$emit('row-selected', index);
    }
  }
};
</script>