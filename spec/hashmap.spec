# frozen_string_literal: true
require_relative '../lib/hashmap'
describe  do


  describe "hash" do
    it "simplifies to a bucket" do
      test = HashMap.new
      hash_code = test.hash('Benjamin')
      index = hash_code.abs % test.capacity
      p index
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

end
# this seems to have been a pure hypothetical