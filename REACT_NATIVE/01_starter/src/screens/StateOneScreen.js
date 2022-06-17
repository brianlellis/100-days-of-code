import ColorChanger from '../components/ColorChanger'
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
  const [counter, setCounter]           = useState(props.initCounter || 0)
  const [colors, setColors]             = useState([])
  const [colorChangers, setColorChange] = useState([{ name: 'Red', rgb: 255}, { name: 'Green', rgb: 255}, { name: 'Blue', rgb: 255}])
  
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
        // div is not used in reactNative as this will not compile to HTML systems
        // https://stackoverflow.com/questions/62853379/is-it-possible-to-use-div-tag-in-react-native-tag
        renderItem={ ({ item }) => <View style={{height: 30, width: 30, backgroundColor: item}}></View> }
      />
      <Button title="Add Color" onPress={() => { setColors([...colors, randomRGB()]) } } />
      <FlatList
        data={colorChangers}
        keyExtractor={ color => color.name }
        renderItem={ ({ item, index }) => (
          <ColorChanger
            name={item.name}
            rgb={item.rgb}
            onIncrease={() => setColorChange(colorChangers[index].rgb+1)}
            onDecrease={() => setColorChange(colorChangers[index].rgb-1)} 
          />
        )}
      />
    </View>
  )
}

export default StateOneScreen