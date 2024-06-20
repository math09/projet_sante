<template>
  <div class="bg-white p-5 rounded-3xl h-full flex overflow-auto">
    <table class="w-full border-separate rounded-xl h-fit table-auto">
        <thead>
          <tr>
            <th class="bg-gray-200 border border-gray-300 p-4 text-left rounded-tl-xl">Nom</th>
            <th class="bg-gray-200 border border-gray-300 p-4 text-left">Prénom</th>
            <th class="bg-gray-200 border border-gray-300 p-4 text-left">Date de naissance</th>
            <th class="bg-gray-200 border border-gray-300 p-4 text-left rounded-tr-xl">Numéro de sécurité sociale</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(person, index) in persons" :key="index" :class="{'bg-gray-100': index % 2 === 0, 'bg-gray-50': index % 2 !== 0, 'bg-gradient-to-r from-teal-500 to-teal-300 text-white': selectedRow === index}"  @click="selectRow(index)">
            <td class="border border-gray-300 p-4" :class="{' rounded-bl-xl': isLastRow(index, persons.length)}">{{ person.nom }}</td>
            <td class="border border-gray-300 p-4">{{ person.prenom }}</td>
            <td class="border border-gray-300 p-4">{{ person.age }}</td>
            <td class="border border-gray-300 p-4" :class="{' rounded-br-xl': isLastRow(index, persons.length)}">{{ person.numSecu }}</td>
          </tr>
        </tbody>
      </table>
  </div>
  
</template>

<script>
export default {
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