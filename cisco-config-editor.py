##############################################################################
#                                                                            #
#                        Cisco Configuration Editor                          #
#                                                                            #
# Copyright (c) 2019  Johnathan Nicolosi <johnathan@nicolosi.space>          #
# All rights reserved                                                        #
#                                                                            #
# Written by Johnathan Nicolosi                                              #
#                                                                            #
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND     #
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE      #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE #
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE    #
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL #
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS    #
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)      #
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT #
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY  #
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF     #
# SUCH DAMAGE.                                                               #
#                                                                            #
##############################################################################

from shutil import copyfile

copyfile('test.txt', 'test2.txt')
with open('test2.txt', 'r') as file:
    data = file.readlines()

print(data)

var_1 = input("Enter variable 1 here:")
var_2 = input("Enter variable 2 here:")
var_3 = input("Enter variable 3 here:")
var_4 = input("Enter variable 4 here:")

line_3 = ("Line three now includes:")
line_5 = ("Line 5 was changed to: ")
line_7 = ("Line 7 is now: ")
line_10 = ("Line 10 has been changed to: ")

data[3] = line_3 + var_1 + "\n"
data[5] = line_5 + var_2 + "\n"
data[7] = line_7 + var_3 + "\n"
data[8] = line_10 + var_4 + "\n"

with open('test2.txt', 'w') as file:
    file.writelines(data)

print(data)