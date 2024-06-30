<template>
  <div class="flex h-full p-5 overflow-auto bg-white rounded-3xl">
    <table class="w-full border-separate table-auto rounded-xl h-fit">
        <thead>
          <tr>
            <th class="p-4 text-left bg-gray-200 border border-gray-300 rounded-tl-xl">Nom</th>
            <th class="p-4 text-left bg-gray-200 border border-gray-300">Prénom</th>
            <th class="p-4 text-left bg-gray-200 border border-gray-300">Date de naissance</th>
            <th class="p-4 text-left bg-gray-200 border border-gray-300 rounded-tr-xl">Numéro de sécurité sociale</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(person, index) in persons" :key="index" :class="{'bg-gray-100': index % 2 === 0, 'bg-gray-50': index % 2 !== 0, 'bg-gradient-to-r from-teal-500 to-teal-300 text-white': selectedRow === index}"  @click="selectRow(index)">
            <td class="p-4 border border-gray-300" :class="{' rounded-bl-xl': isLastRow(index, persons.length)}">{{ person.nom }}</td>
            <td class="p-4 border border-gray-300">{{ person.prenom }}</td>
            <td class="p-4 border border-gray-300">{{ person.age }}</td>
            <td class="p-4 border border-gray-300" :class="{' rounded-br-xl': isLastRow(index, persons.length)}">{{ person.num_secu }}</td>
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