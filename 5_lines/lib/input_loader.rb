
class InputLoader

    attr_reader :lines

    def initialize(txt_file_name="test_input_lines.txt")
        file_path = File.join(File.dirname(__FILE__), '../input/', txt_file_name)
        file = File.open(file_path)
        lines = file.readlines.map(&:chomp)
        
        def handle_line(line)
            pos_1, pos_2 = line.split('->')
            x1, y1 = pos_1.split(',')
            x2, y2 = pos_2.split(',')
            [[x1.to_i(), y1.to_i()], [x2.to_i(), y2.to_i()]]
        end

        @lines = lines.map { |line| handle_line(line) }
        file.close()
    end
end
