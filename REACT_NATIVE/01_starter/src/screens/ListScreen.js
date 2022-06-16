import React from 'react'
import { FlatList, Text, StyleSheet, View } from 'react-native'

const friends    = [1,2,3,4,5,6,7,8,9,10].map( v => ({ name: `Friend #${v}`, age: 3*v }) )
const ListScreen = props => (
  <FlatList
    data={friends}
    // If key not provided then full list will have to be deleted and re-rendered
    keyExtractor={ friend => friend.name }
    renderItem={ ({ item }) => <Text style={styles.textStyle}>{item.name} - Age {item.age}</Text> }
  />
)

const styles = StyleSheet.create({
  textStyle: {
    marginVertical: 50
  }
})

export default ListScreen