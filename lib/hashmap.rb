require_relative 'node'

class HashMap
  attr_accessor :capacity, :buckets
  
  def initialize
    @load_factor = 0.75
    @capacity = 16
    @buckets = Array.new(@capacity)
  end
  # raise IndexError if index.negative? || index >= @buckets.length



  def hash(key)
    hash_code = 0
    prime_number = 31
        
    key.each_char { |char| hash_code = prime_number * hash_code + char.ord }
        
    hash_code
  end

  def generate_index(hash_code)
    hash_code.abs % @capacity
  end
  
  def set(key, value)
    hash_code = hash(key)
    index = generate_index(hash_code)
    @buckets[index] = Node.new(key, value)
    # need guard clause for existing entry
  end

end