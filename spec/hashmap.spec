# frozen_string_literal: true
require_relative '../lib/hashmap'
describe  do


  describe "hash" do
    it "simplifies to a bucket" do
      test = HashMap.new
      hash_code = test.hash('Benjamin')
      index = hash_code.abs % test.capacity
      expect(index).to be_between(0, 15).inclusive
    end
    
    it "Rama becomes '3'" do
      test = HashMap.new
      index = test.hash('Rama')
      expect(index).to eq(3)
    end


    it "Rama and Sita result in a collision" do
      test = HashMap.new
      index = test.hash('Rama')
      index_two = test.hash('Sita')
      expect(index).to eq(index_two)
    end

  end

  describe "set" do
    it "creates a node" do
      test = HashMap.new
      test.set('Rama', 4)
      
      expect(test.buckets[3].value).to eq(4)
    end

    it "overrides a node" do 
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Rama', 5)
      
      expect(test.buckets[3].value).to eq(5)
    end

    it "adds a node when one is in a bucket" do 
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Sita', 5)
      
      return if test.buckets[3].next_node.nil?
      sita_sama = test.buckets[3].next_node
      expect(sita_sama.value).to eq(5)
    end

     it "overrides a linked node" do 
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Sita', 5)
      test.set('Sita', 69)
      
      return if test.buckets[3].next_node.nil?
      sita_sama = test.buckets[3].next_node
      expect(sita_sama.value).to eq(69)
    end

    it "doubles capacity after setting the 13th item" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('ice cream', 'white')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.set('money', 'green')

      expect(test.buckets.length).to eq(32)
    end



  end

  describe "length" do
    
    it "works on a simple set of buckets" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 4)
      
      expect(test.length).to eq(2)
    end

    it "works when one bucket is a linked list" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 4)
      test.set('Sita', 5)
      
      expect(test.length).to eq(3)
    end


  end


  describe "redistribute" do
    it "doesn't trigger for 12 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('ice cream', 'white')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      
      expect(test.redistribute).to eq(nil)
    end

    it "doubles capacity for 13 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('ice cream', 'white')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.set('money', 'green')

      test.redistribute
      
      expect(test.buckets.length).to eq(32)
    end
  end


  describe "get" do
    
    it "works on a simple set of buckets" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 9)
      
      
      expect(test.get('Robin')).to eq(9)
    end

    it "works when one bucket is a linked list" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 4)
      test.set('Sita', 5)
      
      expect(test.get('Sita')).to eq(5)
    end

  end

  describe "has?" do
    
    it "returns false when bucket is empty" do
      test = HashMap.new
      test.set('Rama', 4)
      
      expect(test.has?('Robin')).to eq(false)
    end

    it "returns false when bucket isn't empty but key is wrong" do
      test = HashMap.new
      test.set('Rama', 4)
      
      expect(test.has?('Sita')).to eq(false)
    end

    it "works on a simple set of buckets" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 9)
      
      
      expect(test.has?('Robin')).to eq(true)
    end

    it "works when one bucket is a linked list" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Robin', 4)
      test.set('Sita', 5)
      
      expect(test.has?('Sita')).to eq(true)
    end

  end


  describe "remove" do
    
    it "removes nothing if there is nothing in the bucket" do
      test = HashMap.new
      expect(test.remove('Rama')).to eq(nil)
    end

    it "removes a singular node in a bucket" do
      test = HashMap.new
      test.set('Rama', 4)
      test.remove('Rama')
      
      expect(test.length).to eq(0)
    end

    it "removes the first node in a bucket" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Jackson', 4)
      test.set('Sita', 5)
      test.remove('Rama')

      expect(test.length).to eq(2)
    end

    it "removes the second node in a bucket" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Jackson', 4)
      test.set('Sita', 5)
      test.remove('Jackson')

      expect(test.length).to eq(2)
    end

    it "removes the third node in a bucket" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Jackson', 4)
      test.set('Sita', 5)
      test.remove('Sita')

      expect(test.length).to eq(2)
    end


    it "removes nothing if it is the right bucket but the wrong key" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Sita', 5)

      expect(test.remove('Jackson')).to eq(nil)
    end
  end

  describe "clear" do
    it "removes 12 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('ice cream', 'white')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.clear
      
      expect(test.length).to eq(0)
    end

    it "resets capacity when removing 13 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('ice cream', 'white')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.set('money', 'green')

      test.clear
      
      expect(test.buckets.length).to eq(16)
    end
  end

  describe "keys" do
    it "works on 11 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.keys
      
      output = %w[apple banana carrot dog elephant frog grape hat jacket kite lion]

      expect(test.keys.sort).to eq(output.sort)
    end

  it "works on linked list buckets" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Jackson', 4)
      test.set('Sita', 5)

      output = %w[Rama Jackson Sita]
      
      expect(test.keys.sort).to eq(output.sort)
    end
  end

  describe "values" do
    it "works on 11 items" do
      test = HashMap.new
      test.set('apple', 'red')
      test.set('banana', 'yellow')
      test.set('carrot', 'orange')
      test.set('dog', 'brown')
      test.set('elephant', 'gray')
      test.set('frog', 'green')
      test.set('grape', 'purple')
      test.set('hat', 'black')
      test.set('jacket', 'blue')
      test.set('kite', 'pink')
      test.set('lion', 'golden')
      test.keys
      
      output = %w[red yellow orange brown gray green purple black blue pink golden]

      expect(test.values.sort).to eq(output.sort)
    end

  it "works on linked list buckets" do
      test = HashMap.new
      test.set('Rama', 4)
      test.set('Jackson', 69)
      test.set('Sita', 5)

      output = [4, 69, 5]
      
      expect(test.values.sort).to eq(output.sort)
    end
  end


end
