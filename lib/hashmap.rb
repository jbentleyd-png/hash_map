class HashMap
  attr_accessor :capacity
  
  def initialize
    @load_factor = 0.75
    @capacity = 16
    @buckets = []
  end
  # raise IndexError if index.negative? || index >= @buckets.length

  def generate_index(hash_code)
    hash_code.abs % @capacity
  end

  def hash(key)
    hash_code = 0
    prime_number = 31
        
    key.each_char { |char| hash_code = prime_number * hash_code + char.ord }
        
    hash_code
  end

  

end