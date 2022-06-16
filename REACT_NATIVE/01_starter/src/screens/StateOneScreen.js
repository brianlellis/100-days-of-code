import React, { useState } from 'react'
import {
  Button,
  FlatList,
  StyleSheet,
  Text,
  View,
} from 'react-native'

const randomRGB = () => {
  let rgb_str = "rgb("
  for (let i=0; i<3;i++) rgb_str += i === 2 ? Math.floor(Math.random() * 256) : Math.floor(Math.random() * 256)+','
  return `${rgb_str})`
}

const StateOneScreen = props => {
  const [counter, setCounter] = useState(props.initCounter || 0)
  const [colors, setColors]   = useState([])
  return (
    <View>
      {/* https://reactjs.org/docs/hooks-state.html */}
      {/* Can't use ++/-- for modification of the counter value */}
      <Button title="Increase" onPress={() => { setCounter(counter+1) } } />
      <Button title="Decrease" onPress={() => { setCounter(counter-1) } } />
      <Text>Current Count: {counter}</Text>
      <Button title="Add Color" onPress={() => { setColors([...colors, randomRGB()]) } } />
      <FlatList
        data={colors}
        // If key not provided then full list will have to be deleted and re-rendered
        keyExtractor={ color => color }
        renderItem={ ({ item }) => <View style={{height: 30, width: 30, backgroundColor: item}}></View> }
      />
    </View>
  )
}

export default StateOneScreen